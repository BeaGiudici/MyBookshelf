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