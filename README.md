# Books database

Little exercise to get more familiar with relational databases and the related Python libraries.

## Database structure
The database will collect the books in my bookshelf and is made by these tables:

- **Books**
    |---------|-------|------|------|
    | Book ID | Title | ISBN | Year |
    |---------|-------|------|------|

- **Authors**
    |-----------|------|---------------|---------------|---------|
    | Author ID | Name | Date of Birth | Date of Death | Country |
    |-----------|------|---------------|---------------|---------|

- **Genres**
    |----------|------------|
    | Genre ID | Genre Name |
    |----------|------------|

- **Status**
    |-----------|--------|
    | Status ID | Status |
    |-----------|--------|

### Relationships

There are two 1-N relationships, Author -> Books and Status -> Books, as well as one N-N relationship, Books <-> Genres.