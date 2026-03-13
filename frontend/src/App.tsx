import React, { useEffect, useState } from "react";

type Genre = {
  id: number;
  name: string;
};

type GenresResponse = {
  genres: Genre[];
};

type GenreResponse = {
  genre: Genre;
};

type Author = {
  id: number;
  name: string;
  date_of_birth: string;
  date_of_death: string | null;
  country: string;
};

type AuthorsResponse = {
  authors: Author[];
};

type AuthorResponse = {
  author: Author;
};

type Book = {
  id: number;
  title: string;
  isbn: string;
  year: number;
  author_id: number;
  status_id: number;
};

type BooksResponse = {
  books: Book[];
};

type BookResponse = {
  book: Book;
};

const App: React.FC = () => {
  const [genres, setGenres] = useState<Genre[]>([]);
  const [newGenreName, setNewGenreName] = useState("");

  const [authors, setAuthors] = useState<Author[]>([]);
  const [newAuthor, setNewAuthor] = useState({
    name: "",
    date_of_birth: "",
    date_of_death: "",
    country: ""
  });

  const [books, setBooks] = useState<Book[]>([]);
  const [newBook, setNewBook] = useState({
    title: "",
    isbn: "",
    year: "",
    author_id: "",
    status_id: ""
  });

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const fetchGenres = async () => {
    try {
      setLoading(true);
      setError(null);
      const res = await fetch("/genre/get/all");
      if (!res.ok) {
        throw new Error(`Failed to fetch genres (${res.status})`);
      }
      const data = (await res.json()) as GenresResponse;
      setGenres(data.genres);
    } catch (err) {
      setError((err as Error).message);
    } finally {
      setLoading(false);
    }
  };

  const fetchAuthors = async () => {
    try {
      setLoading(true);
      setError(null);
      const res = await fetch("/author/get/all");
      if (!res.ok) {
        throw new Error(`Failed to fetch authors (${res.status})`);
      }
      const data = (await res.json()) as AuthorsResponse;
      setAuthors(data.authors);
    } catch (err) {
      setError((err as Error).message);
    } finally {
      setLoading(false);
    }
  };

  const fetchBooks = async () => {
    try {
      setLoading(true);
      setError(null);
      const res = await fetch("/book/get/all");
      if (!res.ok) {
        throw new Error(`Failed to fetch books (${res.status})`);
      }
      const data = (await res.json()) as BooksResponse;
      setBooks(data.books);
    } catch (err) {
      setError((err as Error).message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchGenres();
    fetchAuthors();
    fetchBooks();
  }, []);

  const handleAddGenre = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!newGenreName.trim()) return;

    try {
      setLoading(true);
      setError(null);
      const res = await fetch("/genre/create", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ name: newGenreName.trim() })
      });
      if (!res.ok) {
        throw new Error(`Failed to add genre (${res.status})`);
      }
      const data = (await res.json()) as GenreResponse;
      setGenres((prev) => [...prev, data.genre]);
      setNewGenreName("");
    } catch (err) {
      setError((err as Error).message);
    } finally {
      setLoading(false);
    }
  };

  const handleAddAuthor = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!newAuthor.name.trim() || !newAuthor.date_of_birth || !newAuthor.country.trim()) {
      return;
    }

    try {
      setLoading(true);
      setError(null);
      const res = await fetch("/author/create", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          name: newAuthor.name.trim(),
          date_of_birth: newAuthor.date_of_birth,
          date_of_death: newAuthor.date_of_death || null,
          country: newAuthor.country.trim()
        })
      });
      if (!res.ok) {
        throw new Error(`Failed to add author (${res.status})`);
      }
      const data = (await res.json()) as AuthorResponse;
      setAuthors((prev) => [...prev, data.author]);
      setNewAuthor({
        name: "",
        date_of_birth: "",
        date_of_death: "",
        country: ""
      });
    } catch (err) {
      setError((err as Error).message);
    } finally {
      setLoading(false);
    }
  };

  const handleAddBook = async (e: React.FormEvent) => {
    e.preventDefault();
    if (
      !newBook.title.trim() ||
      !newBook.isbn.trim() ||
      !newBook.year ||
      !newBook.author_id ||
      !newBook.status_id
    ) {
      return;
    }

    try {
      setLoading(true);
      setError(null);
      const res = await fetch("/book/create", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          title: newBook.title.trim(),
          isbn: newBook.isbn.trim(),
          year: Number(newBook.year),
          author_id: Number(newBook.author_id),
          status_id: Number(newBook.status_id)
        })
      });
      if (!res.ok) {
        throw new Error(`Failed to add book (${res.status})`);
      }
      const data = (await res.json()) as BookResponse;
      setBooks((prev) => [...prev, data.book]);
      setNewBook({
        title: "",
        isbn: "",
        year: "",
        author_id: "",
        status_id: ""
      });
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
          maxWidth: "720px",
          margin: "0 auto",
          backgroundColor: "white",
          borderRadius: "1rem",
          boxShadow:
            "0 10px 30px rgba(15, 23, 42, 0.08), 0 1px 2px rgba(15, 23, 42, 0.06)",
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
            View and add genres, authors, and books in your database.
          </p>
        </header>

        {/* Genres */}
        <section
          style={{
            display: "flex",
            gap: "1.75rem",
            flexWrap: "wrap",
            alignItems: "flex-start"
          }}
        >
          <form
            onSubmit={handleAddGenre}
            style={{
              flex: "1 1 260px",
              padding: "1.25rem 1.5rem",
              borderRadius: "0.875rem",
              border: "1px solid #e5e7eb",
              backgroundColor: "#f9fafb"
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
              Add a new genre
            </h2>
            <label
              htmlFor="genreName"
              style={{
                display: "block",
                fontSize: "0.8rem",
                fontWeight: 500,
                color: "#6b7280",
                marginBottom: "0.35rem"
              }}
            >
              Genre name
            </label>
            <input
              id="genreName"
              type="text"
              value={newGenreName}
              onChange={(e) => setNewGenreName(e.target.value)}
              placeholder="e.g. Fantasy"
              style={{
                width: "100%",
                padding: "0.6rem 0.75rem",
                borderRadius: "0.6rem",
                border: "1px solid #d1d5db",
                fontSize: "0.9rem",
                outline: "none",
                marginBottom: "0.75rem",
                transition: "border-color 0.15s, box-shadow 0.15s"
              }}
              onFocus={(e) => {
                e.target.style.borderColor = "#6366f1";
                e.target.style.boxShadow =
                  "0 0 0 1px rgba(79, 70, 229, 0.3)";
              }}
              onBlur={(e) => {
                e.target.style.borderColor = "#d1d5db";
                e.target.style.boxShadow = "none";
              }}
            />
            <button
              type="submit"
              disabled={loading || !newGenreName.trim()}
              style={{
                display: "inline-flex",
                alignItems: "center",
                justifyContent: "center",
                gap: "0.35rem",
                padding: "0.55rem 0.9rem",
                borderRadius: "999px",
                border: "none",
                fontSize: "0.85rem",
                fontWeight: 600,
                cursor: loading || !newGenreName.trim() ? "not-allowed" : "pointer",
                background:
                  loading || !newGenreName.trim()
                    ? "#e5e7eb"
                    : "linear-gradient(135deg, #4f46e5, #6366f1)",
                color:
                  loading || !newGenreName.trim() ? "#9ca3af" : "white",
                boxShadow:
                  loading || !newGenreName.trim()
                    ? "none"
                    : "0 8px 18px rgba(79, 70, 229, 0.35)",
                transition:
                  "transform 0.1s ease-out, box-shadow 0.1s ease-out, filter 0.1s"
              }}
            >
              <span>+ Add genre</span>
            </button>
          </form>

          <div
            style={{
              flex: "1.4 1 320px",
              minHeight: "180px"
            }}
          >
            <div
              style={{
                display: "flex",
                justifyContent: "space-between",
                alignItems: "center",
                marginBottom: "0.75rem"
              }}
            >
              <h2
                style={{
                  fontSize: "1rem",
                  fontWeight: 600,
                  color: "#111827"
                }}
              >
                Existing genres
              </h2>
              <button
                type="button"
                onClick={fetchGenres}
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
              <p style={{ fontSize: "0.85rem", color: "#6b7280" }}>
                Loading...
              </p>
            )}

            {error && (
              <p
                style={{
                  fontSize: "0.85rem",
                  color: "#b91c1c",
                  marginBottom: "0.75rem"
                }}
              >
                {error}
              </p>
            )}

            {genres.length === 0 && !loading ? (
              <p
                style={{
                  fontSize: "0.9rem",
                  color: "#9ca3af",
                  fontStyle: "italic"
                }}
              >
                No genres yet. Add your first one using the form on the left.
              </p>
            ) : (
              <ul
                style={{
                  listStyle: "none",
                  padding: 0,
                  margin: 0,
                  display: "grid",
                  gridTemplateColumns: "repeat(auto-fill, minmax(140px, 1fr))",
                  gap: "0.5rem"
                }}
              >
                {genres.map((genre) => (
                  <li
                    key={genre.id}
                    style={{
                      padding: "0.55rem 0.75rem",
                      borderRadius: "0.75rem",
                      backgroundColor: "#f9fafb",
                      border: "1px solid #e5e7eb",
                      fontSize: "0.85rem",
                      color: "#111827"
                    }}
                  >
                    {genre.name}
                  </li>
                ))}
              </ul>
            )}
          </div>
        </section>

        {/* Authors */}
        <section
          style={{
            marginTop: "2rem",
            paddingTop: "1.5rem",
            borderTop: "1px solid #e5e7eb"
          }}
        >
          <div
            style={{
              display: "flex",
              gap: "1.75rem",
              flexWrap: "wrap",
              alignItems: "flex-start"
            }}
          >
            <form
              onSubmit={handleAddAuthor}
              style={{
                flex: "1 1 260px",
                padding: "1.25rem 1.5rem",
                borderRadius: "0.875rem",
                border: "1px solid #e5e7eb",
                backgroundColor: "#f9fafb"
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
                Add a new author
              </h2>

              <label
                htmlFor="authorName"
                style={{
                  display: "block",
                  fontSize: "0.8rem",
                  fontWeight: 500,
                  color: "#6b7280",
                  marginBottom: "0.35rem"
                }}
              >
                Name
              </label>
              <input
                id="authorName"
                type="text"
                value={newAuthor.name}
                onChange={(e) =>
                  setNewAuthor((prev) => ({ ...prev, name: e.target.value }))
                }
                placeholder="e.g. Ursula K. Le Guin"
                style={{
                  width: "100%",
                  padding: "0.6rem 0.75rem",
                  borderRadius: "0.6rem",
                  border: "1px solid #d1d5db",
                  fontSize: "0.9rem",
                  outline: "none",
                  marginBottom: "0.75rem"
                }}
              />

              <label
                htmlFor="authorDob"
                style={{
                  display: "block",
                  fontSize: "0.8rem",
                  fontWeight: 500,
                  color: "#6b7280",
                  marginBottom: "0.35rem"
                }}
              >
                Date of birth
              </label>
              <input
                id="authorDob"
                type="date"
                value={newAuthor.date_of_birth}
                onChange={(e) =>
                  setNewAuthor((prev) => ({
                    ...prev,
                    date_of_birth: e.target.value
                  }))
                }
                style={{
                  width: "100%",
                  padding: "0.6rem 0.75rem",
                  borderRadius: "0.6rem",
                  border: "1px solid #d1d5db",
                  fontSize: "0.9rem",
                  outline: "none",
                  marginBottom: "0.75rem"
                }}
              />

              <label
                htmlFor="authorDod"
                style={{
                  display: "block",
                  fontSize: "0.8rem",
                  fontWeight: 500,
                  color: "#6b7280",
                  marginBottom: "0.35rem"
                }}
              >
                Date of death (optional)
              </label>
              <input
                id="authorDod"
                type="date"
                value={newAuthor.date_of_death}
                onChange={(e) =>
                  setNewAuthor((prev) => ({
                    ...prev,
                    date_of_death: e.target.value
                  }))
                }
                style={{
                  width: "100%",
                  padding: "0.6rem 0.75rem",
                  borderRadius: "0.6rem",
                  border: "1px solid #d1d5db",
                  fontSize: "0.9rem",
                  outline: "none",
                  marginBottom: "0.75rem"
                }}
              />

              <label
                htmlFor="authorCountry"
                style={{
                  display: "block",
                  fontSize: "0.8rem",
                  fontWeight: 500,
                  color: "#6b7280",
                  marginBottom: "0.35rem"
                }}
              >
                Country
              </label>
              <input
                id="authorCountry"
                type="text"
                value={newAuthor.country}
                onChange={(e) =>
                  setNewAuthor((prev) => ({
                    ...prev,
                    country: e.target.value
                  }))
                }
                placeholder="e.g. United States"
                style={{
                  width: "100%",
                  padding: "0.6rem 0.75rem",
                  borderRadius: "0.6rem",
                  border: "1px solid #d1d5db",
                  fontSize: "0.9rem",
                  outline: "none",
                  marginBottom: "0.75rem"
                }}
              />

              <button
                type="submit"
                disabled={
                  loading ||
                  !newAuthor.name.trim() ||
                  !newAuthor.date_of_birth ||
                  !newAuthor.country.trim()
                }
                style={{
                  display: "inline-flex",
                  alignItems: "center",
                  justifyContent: "center",
                  gap: "0.35rem",
                  padding: "0.55rem 0.9rem",
                  borderRadius: "999px",
                  border: "none",
                  fontSize: "0.85rem",
                  fontWeight: 600,
                  cursor:
                    loading ||
                    !newAuthor.name.trim() ||
                    !newAuthor.date_of_birth ||
                    !newAuthor.country.trim()
                      ? "not-allowed"
                      : "pointer",
                  background:
                    loading ||
                    !newAuthor.name.trim() ||
                    !newAuthor.date_of_birth ||
                    !newAuthor.country.trim()
                      ? "#e5e7eb"
                      : "linear-gradient(135deg, #4f46e5, #6366f1)",
                  color:
                    loading ||
                    !newAuthor.name.trim() ||
                    !newAuthor.date_of_birth ||
                    !newAuthor.country.trim()
                      ? "#9ca3af"
                      : "white"
                }}
              >
                <span>+ Add author</span>
              </button>
            </form>

            <div
              style={{
                flex: "1.4 1 320px",
                minHeight: "180px"
              }}
            >
              <div
                style={{
                  display: "flex",
                  justifyContent: "space-between",
                  alignItems: "center",
                  marginBottom: "0.75rem"
                }}
              >
                <h2
                  style={{
                    fontSize: "1rem",
                    fontWeight: 600,
                    color: "#111827"
                  }}
                >
                  Existing authors
                </h2>
                <button
                  type="button"
                  onClick={fetchAuthors}
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

              {authors.length === 0 && !loading ? (
                <p
                  style={{
                    fontSize: "0.9rem",
                    color: "#9ca3af",
                    fontStyle: "italic"
                  }}
                >
                  No authors yet. Add your first one using the form on the left.
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
                  {authors.map((author) => (
                    <li
                      key={author.id}
                      style={{
                        padding: "0.55rem 0.75rem",
                        borderRadius: "0.75rem",
                        backgroundColor: "#f9fafb",
                        border: "1px solid #e5e7eb",
                        fontSize: "0.85rem",
                        color: "#111827"
                      }}
                    >
                      <span style={{ fontWeight: 600 }}>{author.name}</span>
                      <span style={{ color: "#6b7280", marginLeft: "0.35rem" }}>
                        ({author.country})
                      </span>
                    </li>
                  ))}
                </ul>
              )}
            </div>
          </div>
        </section>

        {/* Books */}
        <section
          style={{
            marginTop: "2rem",
            paddingTop: "1.5rem",
            borderTop: "1px solid #e5e7eb"
          }}
        >
          <div
            style={{
              display: "flex",
              gap: "1.75rem",
              flexWrap: "wrap",
              alignItems: "flex-start"
            }}
          >
            <form
              onSubmit={handleAddBook}
              style={{
                flex: "1 1 260px",
                padding: "1.25rem 1.5rem",
                borderRadius: "0.875rem",
                border: "1px solid #e5e7eb",
                backgroundColor: "#f9fafb"
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
                Add a new book
              </h2>

              <label
                htmlFor="bookTitle"
                style={{
                  display: "block",
                  fontSize: "0.8rem",
                  fontWeight: 500,
                  color: "#6b7280",
                  marginBottom: "0.35rem"
                }}
              >
                Title
              </label>
              <input
                id="bookTitle"
                type="text"
                value={newBook.title}
                onChange={(e) =>
                  setNewBook((prev) => ({ ...prev, title: e.target.value }))
                }
                placeholder="e.g. A Wizard of Earthsea"
                style={{
                  width: "100%",
                  padding: "0.6rem 0.75rem",
                  borderRadius: "0.6rem",
                  border: "1px solid #d1d5db",
                  fontSize: "0.9rem",
                  outline: "none",
                  marginBottom: "0.75rem"
                }}
              />

              <label
                htmlFor="bookIsbn"
                style={{
                  display: "block",
                  fontSize: "0.8rem",
                  fontWeight: 500,
                  color: "#6b7280",
                  marginBottom: "0.35rem"
                }}
              >
                ISBN
              </label>
              <input
                id="bookIsbn"
                type="text"
                value={newBook.isbn}
                onChange={(e) =>
                  setNewBook((prev) => ({ ...prev, isbn: e.target.value }))
                }
                style={{
                  width: "100%",
                  padding: "0.6rem 0.75rem",
                  borderRadius: "0.6rem",
                  border: "1px solid #d1d5db",
                  fontSize: "0.9rem",
                  outline: "none",
                  marginBottom: "0.75rem"
                }}
              />

              <label
                htmlFor="bookYear"
                style={{
                  display: "block",
                  fontSize: "0.8rem",
                  fontWeight: 500,
                  color: "#6b7280",
                  marginBottom: "0.35rem"
                }}
              >
                Year
              </label>
              <input
                id="bookYear"
                type="number"
                value={newBook.year}
                onChange={(e) =>
                  setNewBook((prev) => ({ ...prev, year: e.target.value }))
                }
                style={{
                  width: "100%",
                  padding: "0.6rem 0.75rem",
                  borderRadius: "0.6rem",
                  border: "1px solid #d1d5db",
                  fontSize: "0.9rem",
                  outline: "none",
                  marginBottom: "0.75rem"
                }}
              />

              <label
                htmlFor="bookAuthorId"
                style={{
                  display: "block",
                  fontSize: "0.8rem",
                  fontWeight: 500,
                  color: "#6b7280",
                  marginBottom: "0.35rem"
                }}
              >
                Author ID
              </label>
              <input
                id="bookAuthorId"
                type="number"
                value={newBook.author_id}
                onChange={(e) =>
                  setNewBook((prev) => ({ ...prev, author_id: e.target.value }))
                }
                placeholder="Numeric author id"
                style={{
                  width: "100%",
                  padding: "0.6rem 0.75rem",
                  borderRadius: "0.6rem",
                  border: "1px solid #d1d5db",
                  fontSize: "0.9rem",
                  outline: "none",
                  marginBottom: "0.75rem"
                }}
              />

              <label
                htmlFor="bookStatusId"
                style={{
                  display: "block",
                  fontSize: "0.8rem",
                  fontWeight: 500,
                  color: "#6b7280",
                  marginBottom: "0.35rem"
                }}
              >
                Status ID
              </label>
              <input
                id="bookStatusId"
                type="number"
                value={newBook.status_id}
                onChange={(e) =>
                  setNewBook((prev) => ({ ...prev, status_id: e.target.value }))
                }
                placeholder="Numeric status id"
                style={{
                  width: "100%",
                  padding: "0.6rem 0.75rem",
                  borderRadius: "0.6rem",
                  border: "1px solid #d1d5db",
                  fontSize: "0.9rem",
                  outline: "none",
                  marginBottom: "0.75rem"
                }}
              />

              <button
                type="submit"
                disabled={
                  loading ||
                  !newBook.title.trim() ||
                  !newBook.isbn.trim() ||
                  !newBook.year ||
                  !newBook.author_id ||
                  !newBook.status_id
                }
                style={{
                  display: "inline-flex",
                  alignItems: "center",
                  justifyContent: "center",
                  gap: "0.35rem",
                  padding: "0.55rem 0.9rem",
                  borderRadius: "999px",
                  border: "none",
                  fontSize: "0.85rem",
                  fontWeight: 600,
                  cursor:
                    loading ||
                    !newBook.title.trim() ||
                    !newBook.isbn.trim() ||
                    !newBook.year ||
                    !newBook.author_id ||
                    !newBook.status_id
                      ? "not-allowed"
                      : "pointer",
                  background:
                    loading ||
                    !newBook.title.trim() ||
                    !newBook.isbn.trim() ||
                    !newBook.year ||
                    !newBook.author_id ||
                    !newBook.status_id
                      ? "#e5e7eb"
                      : "linear-gradient(135deg, #4f46e5, #6366f1)",
                  color:
                    loading ||
                    !newBook.title.trim() ||
                    !newBook.isbn.trim() ||
                    !newBook.year ||
                    !newBook.author_id ||
                    !newBook.status_id
                      ? "#9ca3af"
                      : "white"
                }}
              >
                <span>+ Add book</span>
              </button>
            </form>

            <div
              style={{
                flex: "1.4 1 320px",
                minHeight: "180px"
              }}
            >
              <div
                style={{
                  display: "flex",
                  justifyContent: "space-between",
                  alignItems: "center",
                  marginBottom: "0.75rem"
                }}
              >
                <h2
                  style={{
                    fontSize: "1rem",
                    fontWeight: 600,
                    color: "#111827"
                  }}
                >
                  Existing books
                </h2>
                <button
                  type="button"
                  onClick={fetchBooks}
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

              {books.length === 0 && !loading ? (
                <p
                  style={{
                    fontSize: "0.9rem",
                    color: "#9ca3af",
                    fontStyle: "italic"
                  }}
                >
                  No books yet. Add your first one using the form on the left.
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
                        padding: "0.55rem 0.75rem",
                        borderRadius: "0.75rem",
                        backgroundColor: "#f9fafb",
                        border: "1px solid #e5e7eb",
                        fontSize: "0.85rem",
                        color: "#111827"
                      }}
                    >
                      <span style={{ fontWeight: 600 }}>{book.title}</span>
                      <span style={{ color: "#6b7280", marginLeft: "0.35rem" }}>
                        ({book.year}) · Author ID {book.author_id} · Status ID{" "}
                        {book.status_id}
                      </span>
                    </li>
                  ))}
                </ul>
              )}
            </div>
          </div>
        </section>
      </div>
    </div>
  );
};

export default App;

