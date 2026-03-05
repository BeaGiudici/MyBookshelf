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

```
┌──────────────────────┐       ┌──────────────────────────┐       ┌─────────────────┐
│       Authors        │       │          Books           │       │     Status      │
├──────────────────────┤       ├──────────────────────────┤       ├─────────────────┤
│ Author ID (PK)       │──1:N─>│ Book ID (PK)             │<─1:N──│ Status ID (PK)  │
│ Name                 │       │ Title                    │       │ Status          │
│ Date of Birth        │       │ ISBN                     │       └─────────────────┘
│ Date of Death        │       │ Year                     │
│ Country              │       │ Author ID (FK)           │
└──────────────────────┘       │ Status ID (FK)           │
                               └────────────┬─────────────┘
                                            │
                                           1:N
                                            │
                               ┌────────────┴─────────────┐
                               │       Book_Genres        │
                               ├──────────────────────────┤
                               │ Book ID (FK)             │
                               │ Genre ID (FK)            │
                               └────────────┬─────────────┘
                                            │
                                           N:1
                                            │
                               ┌────────────┴─────────────┐
                               │         Genres           │
                               ├──────────────────────────┤
                               │ Genre ID (PK)            │
                               │ Genre Name               │
                               └──────────────────────────┘
```

[![Mermaid view here](https://mermaid.ink/img/pako:eNp9kU1vwjAMQP9K5HOLSNs0TW4w0CZtKxIflymXbMmggiYopNK2wn9f2jIOO-CDJTvv2VLcwodVGjjEcSyMr_xBczS1dn9CM-nluzxpYfo3YbSbVXLrZC0MCjHZrJ8WyxU6n-PYtmi6WDyvEEcCMC8FDMxqPVlv7iND80oIeKnMHoXFBy3gP_o4L5fze2zJccdCBFtXKeDeNTqCWrtadiW03RwBfqfroHSGkm7fKZfgHKV5s7b-05xttjvgn_JwClVzVNLr6wfcEG2Udg-2MR44YayfAbyFL-AJzkaEZQlLx4yOCSloBN_AcWjjPCM0T1NKcsbwJYKffu14RIuMspzijBZJyEUEWlXeutfhRv2pLr8-zoB1?type=png)](https://mermaid.live/edit#pako:eNp9kU1vwjAMQP9K5HOLSNs0TW4w0CZtKxIflymXbMmggiYopNK2wn9f2jIOO-CDJTvv2VLcwodVGjjEcSyMr_xBczS1dn9CM-nluzxpYfo3YbSbVXLrZC0MCjHZrJ8WyxU6n-PYtmi6WDyvEEcCMC8FDMxqPVlv7iND80oIeKnMHoXFBy3gP_o4L5fze2zJccdCBFtXKeDeNTqCWrtadiW03RwBfqfroHSGkm7fKZfgHKV5s7b-05xttjvgn_JwClVzVNLr6wfcEG2Udg-2MR44YayfAbyFL-AJzkaEZQlLx4yOCSloBN_AcWjjPCM0T1NKcsbwJYKffu14RIuMspzijBZJyEUEWlXeutfhRv2pLr8-zoB1)