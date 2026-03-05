# Create fake entries for the database

from models.book import Book
from models.author import Author
from models.genre import Genre
from models.status import Status
from faker import Faker
import warnings

warnings.filterwarnings("ignore")

Faker.seed(42)
fake = Faker()

# Fixed sets for lookup tables
genres = ["Fiction", "Non-Fiction", "Science Fiction", "Fantasy", "Mystery", "Biography", "History"]
statuses = ["TBR", "Reading", "Read"]

# Create genres, statuses, then authors, then books linking them together

def create_fake_books(session):
    all_genres = session.query(Genre).all()
    for _ in range(10):
        book = Book(
            title=fake.catch_phrase(),
            isbn=fake.isbn13(),
            year=fake.year(),
            author=fake.random_element(elements=session.query(Author).all()),
            genres=fake.random_elements(elements=all_genres, length=2, unique=True),
            status=fake.random_element(elements=session.query(Status).all()),
        )
        session.add(book)
        session.commit()
    print("Fake books created successfully")

def create_fake_authors(session):
    for _ in range(5):
        author = Author(
            name=fake.name(),
            date_of_birth=fake.date_of_birth(),
            #date_of_death=fake.date_of_birth(),
            country=fake.country(),
        )
        session.add(author)
        session.commit()
    print("Fake authors created successfully")

def create_fake_genres(session):
    for g in genres:
        genre = Genre(name=g)
        session.add(genre)
        session.commit()
    print("Fake genres created successfully")

def create_fake_statuses(session):
    for s in statuses:
        status = Status(name=s)
        session.add(status)
        session.commit()
    print("Fake statuses created successfully")


def create_fake_entries(session):
    create_fake_genres(session)
    create_fake_statuses(session)
    create_fake_authors(session)
    create_fake_books(session)
    print("Fake entries created successfully")

if __name__ == "__main__":
    from sqlmodel import create_engine, Session
    from dotenv import load_dotenv
    import os

    load_dotenv()

    db_url = os.getenv("DB_URL")
    engine = create_engine(db_url)

    with Session(engine) as session:
        create_fake_entries(session)