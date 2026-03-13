# Books database

Little exercise to get more familiar with relational databases and the related Python libraries.

## Database structure
The database will collect the books in my bookshelf and is made by these tables:

- **Books**
    | Book ID | Title | ISBN | Year |
    |---------|-------|------|------|

- **Authors**
    | Author ID | Name | Date of Birth | Date of Death | Country |
    |-----------|------|---------------|---------------|---------|

- **Genres**
    | Genre ID | Genre Name |
    |----------|------------|

- **Status**
    | Status ID | Status |
    |-----------|--------|

### Relationships

- Authors ──1:N──> Books      (one author has many books)
- Status  ──1:N──> Books      (one status applies to many books)
- Books   <─N:N─> Genres      (many books have many genres, via Book_Genres)

Schematically, we have:

```mermaid
---
title: Books Database
---

erDiagram
    AUTHORS {
        int author_id PK
        string name
        date date_of_birth
        date date_of_death
        string country
    }
    BOOKS {
        int book_id PK
        string title
        string isbn
        int year
        int author_id FK
        int status_id FK
    }
    STATUS {
        int status_id PK
        string status
    }
    GENRES {
        int genre_id PK
        string genre_name
    }
    BOOKGENRELINK {
        int book_id FK
        int genre_id FK
    }
    AUTHORS ||--o{ BOOKS : "1:N"
    STATUS ||--o{ BOOKS : "1:N"
    BOOKS ||--o{ BOOKGENRELINK : "1:N"
    GENRES ||--o{ BOOKGENRELINK : "N:1"
```

## Frontend

There is a very small React + Vite frontend in the `frontend` folder that talks to the FastAPI backend.

- **Install dependencies** (run from the project root):

  ```bash
  cd frontend
  npm install
  ```

- **Run the backend** (from the project root, example with uv):

  ```bash
  uv run uvicorn src.api:app --reload
  ```

- **Run the frontend dev server**:

  ```bash
  cd frontend
  npm run dev
  ```

The frontend expects the API to be available at `http://localhost:8000` and uses these endpoints:

- `GET /genre/get/all` to fetch all genres
- `POST /genre/create` with body `{ "name": string }` to create a new genre
