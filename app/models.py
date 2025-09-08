from pydantic import BaseModel, field_validator, Field
from enum import Enum
from typing import Optional

class Status(str, Enum):
    read = 'read'
    toBeRead = 'to-be-read'
    reading = 'reading'

# Create book
class BookCreate(BaseModel):
    title : str = Field(None, min_length=1)
    author : str = Field(None, min_length=1)
    isbn : str = Field(None, min_length=1)

# Update Book
class BookUpdate(BaseModel):
    title : Optional[str] = Field(None, min_length=1)
    author : Optional[str] = Field(None, min_length=1)
    genre : Optional[str]
    year : Optional[int]
    isbn : str
    type : Optional[str]
    status : Status
    description : Optional[str]

# Full Book model
class Book(BaseModel):
    title : str
    author : str
    genre : Optional[str]
    year : Optional[int]
    isbn : str
    type : Optional[str]
    status : Status
    description : Optional[str]

    @field_validator('isbn')
    def validate_isbn(num):
        digits = num.replace('-','')
        if len(digits) not in (10,13):
            raise ValueError('ISBN code must have 10 or 13 digits.')
        if not digits.isdigit():
            raise ValueError('ISBN code must contain only digits.')
        return num
