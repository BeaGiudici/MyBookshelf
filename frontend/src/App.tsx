import React, { useEffect, useState } from "react";

type Genre = { id: number; name: string };
type Author = {
  id: number;
  name: string;
  date_of_birth: string;
  date_of_death: string | null;
  country: string;
};
type Status = { id: number; name: string };
type Book = {
  id: number;
  title: string;
  isbn: string;
  year: number;
  author_id: number;
  status_id: number;
};

const inputStyle: React.CSSProperties = {
  width: "100%",
  padding: "0.6rem 0.75rem",
  borderRadius: "0.6rem",
  border: "1px solid #d1d5db",
  fontSize: "0.9rem",
  outline: "none",
  marginBottom: "0.75rem"
};

const labelStyle: React.CSSProperties = {
  display: "block",
  fontSize: "0.8rem",
  fontWeight: 500,
  color: "#6b7280",
  marginBottom: "0.35rem"
};

const cardStyle: React.CSSProperties = {
  padding: "1.25rem 1.5rem",
  borderRadius: "0.875rem",
  border: "1px solid #e5e7eb",
  backgroundColor: "#f9fafb"
};

const pillStyle: React.CSSProperties = {
  padding: "0.55rem 0.75rem",
  borderRadius: "0.75rem",
  backgroundColor: "#f9fafb",
  border: "1px solid #e5e7eb",
  fontSize: "0.85rem",
  color: "#111827"
};

const deleteBtnStyle: React.CSSProperties = {
  background: "none",
  border: "none",
  cursor: "pointer",
  padding: "0.25rem",
  borderRadius: "0.375rem",
  color: "#9ca3af",
  fontSize: "0.95rem",
  lineHeight: 1,
  flexShrink: 0,
  transition: "color 0.15s"
};

function submitBtnStyle(disabled: boolean): React.CSSProperties {
  return {
    display: "inline-flex",
    alignItems: "center",
    justifyContent: "center",
    padding: "0.55rem 0.9rem",
    borderRadius: "999px",
    border: "none",
    fontSize: "0.85rem",
    fontWeight: 600,
    cursor: disabled ? "not-allowed" : "pointer",
    background: disabled
      ? "#e5e7eb"
      : "linear-gradient(135deg, #4f46e5, #6366f1)",
    color: disabled ? "#9ca3af" : "white",
    boxShadow: disabled ? "none" : "0 8px 18px rgba(79,70,229,0.35)",
    transition: "transform 0.1s, box-shadow 0.1s"
  };
}

async function jsonOrThrow(res: Response): Promise<unknown> {
  const contentType = res.headers.get("content-type") ?? "";
  if (!contentType.includes("application/json")) {
    throw new Error(
      `Expected JSON but got "${contentType}". Is the backend running?`
    );
  }
  if (!res.ok) {
    const body = await res.json().catch(() => ({}));
    throw new Error(
      (body as { detail?: string }).detail ?? `Request failed (${res.status})`
    );
  }
  return res.json();
}

const App: React.FC = () => {
  const [genres, setGenres] = useState<Genre[]>([]);
  const [authors, setAuthors] = useState<Author[]>([]);
  const [statuses, setStatuses] = useState<Status[]>([]);
  const [books, setBooks] = useState<Book[]>([]);

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [success, setSuccess] = useState<string | null>(null);

  // Unified form state
  const [bookTitle, setBookTitle] = useState("");
  const [bookIsbn, setBookIsbn] = useState("");
  const [bookYear, setBookYear] = useState("");

  const [authorMode, setAuthorMode] = useState<"existing" | "new">("existing");
  const [selectedAuthorId, setSelectedAuthorId] = useState("");
  const [newAuthorName, setNewAuthorName] = useState("");
  const [newAuthorDob, setNewAuthorDob] = useState("");
  const [newAuthorDod, setNewAuthorDod] = useState("");
  const [newAuthorCountry, setNewAuthorCountry] = useState("");

  const [selectedStatusId, setSelectedStatusId] = useState("");

  const [selectedGenreIds, setSelectedGenreIds] = useState<number[]>([]);
  const [newGenreName, setNewGenreName] = useState("");

  // Fetchers
  const fetchAll = async () => {
    setLoading(true);
    setError(null);
    try {
      const [gData, aData, sData, bData] = await Promise.all([
        fetch("/genre/get/all").then(jsonOrThrow),
        fetch("/author/get/all").then(jsonOrThrow),
        fetch("/status/get/all").then(jsonOrThrow),
        fetch("/book/get/all").then(jsonOrThrow)
      ]) as [
        { genres: Genre[] },
        { authors: Author[] },
        { statuses: Status[] },
        { books: Book[] }
      ];
      setGenres(gData.genres);
      setAuthors(aData.authors);
      setStatuses(sData.statuses);
      setBooks(bData.books);
    } catch (err) {
      setError((err as Error).message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchAll();
  }, []);

  // Helpers to look up names by id for the book list
  const authorName = (id: number) =>
    authors.find((a) => a.id === id)?.name ?? `Author #${id}`;
  const statusName = (id: number) =>
    statuses.find((s) => s.id === id)?.name ?? `Status #${id}`;

  const toggleGenre = (id: number) => {
    setSelectedGenreIds((prev) =>
      prev.includes(id) ? prev.filter((g) => g !== id) : [...prev, id]
    );
  };

  const handleAddGenre = async () => {
    if (!newGenreName.trim()) return;
    try {
      const data = (await fetch("/genre/create", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name: newGenreName.trim() })
      }).then(jsonOrThrow)) as { genre: Genre };
      setGenres((prev) => [...prev, data.genre]);
      setSelectedGenreIds((prev) => [...prev, data.genre.id]);
      setNewGenreName("");
    } catch (err) {
      setError((err as Error).message);
    }
  };

  const handleDeleteBook = async (id: number) => {
    try {
      setError(null);
      await fetch(`/book/delete?book_id=${id}`, { method: "DELETE" }).then(jsonOrThrow);
      setBooks((prev) => prev.filter((b) => b.id !== id));
    } catch (err) {
      setError((err as Error).message);
    }
  };

  const handleDeleteAuthor = async (id: number) => {
    try {
      setError(null);
      await fetch(`/author/delete?author_id=${id}`, { method: "DELETE" }).then(jsonOrThrow);
      setAuthors((prev) => prev.filter((a) => a.id !== id));
      const booksData = (await fetch("/book/get/all").then(jsonOrThrow)) as {
        books: Book[];
      };
      setBooks(booksData.books);
    } catch (err) {
      setError((err as Error).message);
    }
  };

  const handleDeleteGenre = async (id: number) => {
    try {
      setError(null);
      await fetch(`/genre/delete?genre_id=${id}`, { method: "DELETE" }).then(jsonOrThrow);
      setGenres((prev) => prev.filter((g) => g.id !== id));
      setSelectedGenreIds((prev) => prev.filter((gid) => gid !== id));
    } catch (err) {
      setError((err as Error).message);
    }
  };

  const canSubmit =
    !loading &&
    bookTitle.trim() &&
    bookIsbn.trim() &&
    bookYear &&
    selectedStatusId &&
    (authorMode === "existing"
      ? !!selectedAuthorId
      : newAuthorName.trim() && newAuthorDob && newAuthorCountry.trim());

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!canSubmit) return;

    try {
      setLoading(true);
      setError(null);
      setSuccess(null);

      // Step 1: resolve author_id
      let authorId: number;

      if (authorMode === "existing") {
        authorId = Number(selectedAuthorId);
      } else {
        const data = (await fetch("/author/create", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            name: newAuthorName.trim(),
            date_of_birth: newAuthorDob,
            date_of_death: newAuthorDod || null,
            country: newAuthorCountry.trim()
          })
        }).then(jsonOrThrow)) as { author: Author };
        authorId = data.author.id;
        setAuthors((prev) => [...prev, data.author]);
      }

      // Step 2: create the book
      const bookData = (await fetch("/book/create", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          title: bookTitle.trim(),
          isbn: bookIsbn.trim(),
          year: Number(bookYear),
          author_id: authorId,
          status_id: Number(selectedStatusId)
        })
      }).then(jsonOrThrow)) as { book: Book };
      setBooks((prev) => [...prev, bookData.book]);

      // Reset form
      setBookTitle("");
      setBookIsbn("");
      setBookYear("");
      setAuthorMode("existing");
      setSelectedAuthorId("");
      setNewAuthorName("");
      setNewAuthorDob("");
      setNewAuthorDod("");
      setNewAuthorCountry("");
      setSelectedStatusId("");
      setSelectedGenreIds([]);
      setNewGenreName("");
      setSuccess(`"${bookData.book.title}" added successfully!`);
      setTimeout(() => setSuccess(null), 3000);
    } catch (err) {
      setError((err as Error).message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      style={{
        minHeight: "100vh",
        fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, sans-serif",
        background:
          "radial-gradient(circle at top left, #f5f3ff 0, #eef2ff 30%, #eff6ff 60%, #f9fafb 100%)",
        padding: "2rem"
      }}
    >
      <div
        style={{
          maxWidth: "780px",
          margin: "0 auto",
          backgroundColor: "white",
          borderRadius: "1rem",
          boxShadow:
            "0 10px 30px rgba(15,23,42,0.08), 0 1px 2px rgba(15,23,42,0.06)",
          padding: "2rem 2.5rem"
        }}
      >
        <header style={{ marginBottom: "1.5rem" }}>
          <h1
            style={{
              fontSize: "1.75rem",
              fontWeight: 700,
              color: "#111827",
              marginBottom: "0.25rem"
            }}
          >
            My Bookshelf
          </h1>
          <p style={{ color: "#6b7280", fontSize: "0.9rem" }}>
            Add a book with its author, status, and genres -- all in one form.
          </p>
        </header>

        {error && (
          <p
            style={{
              fontSize: "0.85rem",
              color: "#b91c1c",
              marginBottom: "0.75rem",
              padding: "0.5rem 0.75rem",
              backgroundColor: "#fef2f2",
              borderRadius: "0.5rem"
            }}
          >
            {error}
          </p>
        )}

        {success && (
          <p
            style={{
              fontSize: "0.85rem",
              color: "#15803d",
              marginBottom: "0.75rem",
              padding: "0.5rem 0.75rem",
              backgroundColor: "#f0fdf4",
              borderRadius: "0.5rem"
            }}
          >
            {success}
          </p>
        )}

        {/* ── Unified "Add a book" form ── */}
        <form onSubmit={handleSubmit} style={cardStyle}>
          <h2
            style={{
              fontSize: "1.1rem",
              fontWeight: 600,
              color: "#111827",
              marginBottom: "1rem"
            }}
          >
            Add a new book
          </h2>

          {/* Book details */}
          <div
            style={{
              display: "grid",
              gridTemplateColumns: "1fr 1fr",
              gap: "0 1rem"
            }}
          >
            <div style={{ gridColumn: "1 / -1" }}>
              <label htmlFor="title" style={labelStyle}>
                Title
              </label>
              <input
                id="title"
                type="text"
                value={bookTitle}
                onChange={(e) => setBookTitle(e.target.value)}
                placeholder="e.g. A Wizard of Earthsea"
                style={inputStyle}
              />
            </div>

            <div>
              <label htmlFor="isbn" style={labelStyle}>
                ISBN
              </label>
              <input
                id="isbn"
                type="text"
                value={bookIsbn}
                onChange={(e) => setBookIsbn(e.target.value)}
                style={inputStyle}
              />
            </div>

            <div>
              <label htmlFor="year" style={labelStyle}>
                Year
              </label>
              <input
                id="year"
                type="number"
                value={bookYear}
                onChange={(e) => setBookYear(e.target.value)}
                style={inputStyle}
              />
            </div>
          </div>

          {/* Author section */}
          <fieldset
            style={{
              border: "1px solid #e5e7eb",
              borderRadius: "0.75rem",
              padding: "1rem 1.25rem",
              marginBottom: "1rem"
            }}
          >
            <legend
              style={{
                fontSize: "0.85rem",
                fontWeight: 600,
                color: "#374151",
                padding: "0 0.35rem"
              }}
            >
              Author
            </legend>

            <div
              style={{
                display: "flex",
                gap: "0.5rem",
                marginBottom: "0.75rem"
              }}
            >
              <button
                type="button"
                onClick={() => setAuthorMode("existing")}
                style={{
                  padding: "0.35rem 0.75rem",
                  borderRadius: "999px",
                  border: "1px solid #d1d5db",
                  fontSize: "0.8rem",
                  cursor: "pointer",
                  fontWeight: authorMode === "existing" ? 600 : 400,
                  backgroundColor:
                    authorMode === "existing" ? "#eef2ff" : "white",
                  color: authorMode === "existing" ? "#4f46e5" : "#6b7280",
                  borderColor:
                    authorMode === "existing" ? "#6366f1" : "#d1d5db"
                }}
              >
                Pick existing
              </button>
              <button
                type="button"
                onClick={() => setAuthorMode("new")}
                style={{
                  padding: "0.35rem 0.75rem",
                  borderRadius: "999px",
                  border: "1px solid #d1d5db",
                  fontSize: "0.8rem",
                  cursor: "pointer",
                  fontWeight: authorMode === "new" ? 600 : 400,
                  backgroundColor: authorMode === "new" ? "#eef2ff" : "white",
                  color: authorMode === "new" ? "#4f46e5" : "#6b7280",
                  borderColor: authorMode === "new" ? "#6366f1" : "#d1d5db"
                }}
              >
                Create new
              </button>
            </div>

            {authorMode === "existing" ? (
              <div>
                <label htmlFor="existingAuthor" style={labelStyle}>
                  Select author
                </label>
                <select
                  id="existingAuthor"
                  value={selectedAuthorId}
                  onChange={(e) => setSelectedAuthorId(e.target.value)}
                  style={{ ...inputStyle, cursor: "pointer" }}
                >
                  <option value="">-- choose --</option>
                  {authors.map((a) => (
                    <option key={a.id} value={a.id}>
                      {a.name} ({a.country})
                    </option>
                  ))}
                </select>
              </div>
            ) : (
              <div
                style={{
                  display: "grid",
                  gridTemplateColumns: "1fr 1fr",
                  gap: "0 1rem"
                }}
              >
                <div style={{ gridColumn: "1 / -1" }}>
                  <label htmlFor="newAuthorName" style={labelStyle}>
                    Name
                  </label>
                  <input
                    id="newAuthorName"
                    type="text"
                    value={newAuthorName}
                    onChange={(e) => setNewAuthorName(e.target.value)}
                    placeholder="e.g. Ursula K. Le Guin"
                    style={inputStyle}
                  />
                </div>
                <div>
                  <label htmlFor="newAuthorDob" style={labelStyle}>
                    Date of birth
                  </label>
                  <input
                    id="newAuthorDob"
                    type="date"
                    value={newAuthorDob}
                    onChange={(e) => setNewAuthorDob(e.target.value)}
                    style={inputStyle}
                  />
                </div>
                <div>
                  <label htmlFor="newAuthorDod" style={labelStyle}>
                    Date of death (optional)
                  </label>
                  <input
                    id="newAuthorDod"
                    type="date"
                    value={newAuthorDod}
                    onChange={(e) => setNewAuthorDod(e.target.value)}
                    style={inputStyle}
                  />
                </div>
                <div style={{ gridColumn: "1 / -1" }}>
                  <label htmlFor="newAuthorCountry" style={labelStyle}>
                    Country
                  </label>
                  <input
                    id="newAuthorCountry"
                    type="text"
                    value={newAuthorCountry}
                    onChange={(e) => setNewAuthorCountry(e.target.value)}
                    placeholder="e.g. United States"
                    style={inputStyle}
                  />
                </div>
              </div>
            )}
          </fieldset>

          {/* Status */}
          <div>
            <label htmlFor="status" style={labelStyle}>
              Status
            </label>
            <select
              id="status"
              value={selectedStatusId}
              onChange={(e) => setSelectedStatusId(e.target.value)}
              style={{ ...inputStyle, cursor: "pointer" }}
            >
              <option value="">-- choose --</option>
              {statuses.map((s) => (
                <option key={s.id} value={s.id}>
                  {s.name}
                </option>
              ))}
            </select>
          </div>

          {/* Genres (multi-select via toggleable pills) */}
          <div style={{ marginBottom: "1rem" }}>
            <span style={labelStyle}>Genres (click to toggle)</span>
            {genres.length === 0 ? (
              <p
                style={{
                  fontSize: "0.8rem",
                  color: "#9ca3af",
                  fontStyle: "italic"
                }}
              >
                No genres available yet.
              </p>
            ) : (
              <div style={{ display: "flex", flexWrap: "wrap", gap: "0.4rem" }}>
                {genres.map((g) => {
                  const selected = selectedGenreIds.includes(g.id);
                  return (
                    <button
                      key={g.id}
                      type="button"
                      onClick={() => toggleGenre(g.id)}
                      style={{
                        padding: "0.35rem 0.65rem",
                        borderRadius: "999px",
                        fontSize: "0.8rem",
                        cursor: "pointer",
                        border: selected
                          ? "1px solid #6366f1"
                          : "1px solid #d1d5db",
                        backgroundColor: selected ? "#eef2ff" : "white",
                        color: selected ? "#4f46e5" : "#374151",
                        fontWeight: selected ? 600 : 400
                      }}
                    >
                      {g.name}
                    </button>
                  );
                })}
              </div>
            )}
            <div
              style={{
                display: "flex",
                gap: "0.5rem",
                marginTop: "0.5rem",
                alignItems: "center"
              }}
            >
              <input
                type="text"
                value={newGenreName}
                onChange={(e) => setNewGenreName(e.target.value)}
                placeholder="New genre name"
                onKeyDown={(e) => {
                  if (e.key === "Enter") {
                    e.preventDefault();
                    handleAddGenre();
                  }
                }}
                style={{
                  ...inputStyle,
                  marginBottom: 0,
                  flex: 1
                }}
              />
              <button
                type="button"
                onClick={handleAddGenre}
                disabled={!newGenreName.trim()}
                style={{
                  ...submitBtnStyle(!newGenreName.trim()),
                  padding: "0.5rem 0.75rem",
                  fontSize: "0.8rem",
                  whiteSpace: "nowrap"
                }}
              >
                + Add genre
              </button>
            </div>
          </div>

          <button type="submit" disabled={!canSubmit} style={submitBtnStyle(!canSubmit)}>
            + Add book
          </button>
        </form>

        {/* ── Existing books ── */}
        <section style={{ marginTop: "2rem" }}>
          <div
            style={{
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
              marginBottom: "0.75rem"
            }}
          >
            <h2 style={{ fontSize: "1rem", fontWeight: 600, color: "#111827" }}>
              Books
            </h2>
            <button
              type="button"
              onClick={fetchAll}
              disabled={loading}
              style={{
                fontSize: "0.8rem",
                padding: "0.35rem 0.7rem",
                borderRadius: "999px",
                border: "1px solid #e5e7eb",
                backgroundColor: "white",
                cursor: loading ? "not-allowed" : "pointer",
                color: "#4b5563"
              }}
            >
              Refresh
            </button>
          </div>

          {loading && (
            <p style={{ fontSize: "0.85rem", color: "#6b7280" }}>Loading...</p>
          )}

          {books.length === 0 && !loading ? (
            <p
              style={{
                fontSize: "0.9rem",
                color: "#9ca3af",
                fontStyle: "italic"
              }}
            >
              No books yet. Use the form above to add your first one.
            </p>
          ) : (
            <ul
              style={{
                listStyle: "none",
                padding: 0,
                margin: 0,
                display: "flex",
                flexDirection: "column",
                gap: "0.4rem"
              }}
            >
              {books.map((book) => (
                <li
                  key={book.id}
                  style={{
                    ...pillStyle,
                    display: "flex",
                    justifyContent: "space-between",
                    alignItems: "center"
                  }}
                >
                  <div>
                    <span style={{ fontWeight: 600 }}>{book.title}</span>
                    <span style={{ color: "#6b7280", marginLeft: "0.35rem" }}>
                      ({book.year}) · {authorName(book.author_id)} ·{" "}
                      {statusName(book.status_id)}
                    </span>
                  </div>
                  <button
                    type="button"
                    title="Delete book"
                    onClick={() => handleDeleteBook(book.id)}
                    onMouseEnter={(e) => (e.currentTarget.style.color = "#dc2626")}
                    onMouseLeave={(e) => (e.currentTarget.style.color = "#9ca3af")}
                    style={deleteBtnStyle}
                  >
                    &#x2715;
                  </button>
                </li>
              ))}
            </ul>
          )}
        </section>

        {/* ── Existing authors ── */}
        <section
          style={{
            marginTop: "1.5rem",
            paddingTop: "1.25rem",
            borderTop: "1px solid #e5e7eb"
          }}
        >
          <h2
            style={{
              fontSize: "1rem",
              fontWeight: 600,
              color: "#111827",
              marginBottom: "0.75rem"
            }}
          >
            Authors
          </h2>
          {authors.length === 0 ? (
            <p
              style={{
                fontSize: "0.9rem",
                color: "#9ca3af",
                fontStyle: "italic"
              }}
            >
              No authors yet.
            </p>
          ) : (
            <ul
              style={{
                listStyle: "none",
                padding: 0,
                margin: 0,
                display: "flex",
                flexDirection: "column",
                gap: "0.4rem"
              }}
            >
              {authors.map((a) => (
                <li
                  key={a.id}
                  style={{
                    ...pillStyle,
                    display: "flex",
                    justifyContent: "space-between",
                    alignItems: "center"
                  }}
                >
                  <div>
                    <span style={{ fontWeight: 600 }}>{a.name}</span>
                    <span style={{ color: "#6b7280", marginLeft: "0.35rem" }}>
                      ({a.country})
                    </span>
                  </div>
                  <button
                    type="button"
                    title="Delete author"
                    onClick={() => handleDeleteAuthor(a.id)}
                    onMouseEnter={(e) => (e.currentTarget.style.color = "#dc2626")}
                    onMouseLeave={(e) => (e.currentTarget.style.color = "#9ca3af")}
                    style={deleteBtnStyle}
                  >
                    &#x2715;
                  </button>
                </li>
              ))}
            </ul>
          )}
        </section>

        {/* ── Existing genres ── */}
        <section
          style={{
            marginTop: "1.5rem",
            paddingTop: "1.25rem",
            borderTop: "1px solid #e5e7eb"
          }}
        >
          <h2
            style={{
              fontSize: "1rem",
              fontWeight: 600,
              color: "#111827",
              marginBottom: "0.75rem"
            }}
          >
            Genres
          </h2>
          {genres.length === 0 ? (
            <p
              style={{
                fontSize: "0.9rem",
                color: "#9ca3af",
                fontStyle: "italic"
              }}
            >
              No genres yet.
            </p>
          ) : (
            <div
              style={{
                display: "flex",
                flexWrap: "wrap",
                gap: "0.4rem"
              }}
            >
              {genres.map((g) => (
                <span
                  key={g.id}
                  style={{
                    ...pillStyle,
                    display: "inline-flex",
                    alignItems: "center",
                    gap: "0.3rem"
                  }}
                >
                  {g.name}
                  <button
                    type="button"
                    title="Delete genre"
                    onClick={() => handleDeleteGenre(g.id)}
                    onMouseEnter={(e) => (e.currentTarget.style.color = "#dc2626")}
                    onMouseLeave={(e) => (e.currentTarget.style.color = "#9ca3af")}
                    style={deleteBtnStyle}
                  >
                    &#x2715;
                  </button>
                </span>
              ))}
            </div>
          )}
        </section>
      </div>
    </div>
  );
};

export default App;
