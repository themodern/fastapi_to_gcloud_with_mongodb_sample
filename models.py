import uuid
from typing import Optional
from pydantic import BaseModel, Field

class Book(BaseModel):
    """
    A class representing a book.

    Attributes:
    -----------
    id : str
        The unique identifier for the book.
    title : str
        The title of the book.
    author : str
        The author of the book.
    synopsis : str
        A brief summary of the book's contents.
    """
    # Define the attributes of the Book class using Pydantic's 'Field' class
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    title: str = Field(...)
    author: str = Field(...)
    synopsis: str = Field(...)


    # Pydantic configuration settings for the 'Book' model
    class Config:
        allow_population_by_field_name = True # Allows initializing attributes by field name (e.g., '{"title": "Book Title"}')
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "title": "Don Quixote",
                "author": "Miguel de Cervantes",
                "synopsis": "..."
            }
        }


class BookUpdate(BaseModel):
    title: Optional[str]
    author: Optional[str]
    synopsis: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "title": "Don Quixote",
                "author": "Miguel de Cervantes",
                "synopsis": "Don Quixote is a Spanish novel by Miguel de Cervantes..."
            }
        }
