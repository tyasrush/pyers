from collections import namedtuple
from datetime import datetime
from typing import Optional

Book = namedtuple('book_', ['id', 'title', 'isbn', 'created_at', 'updated_at'])

class Book1:
    id: str
    title: str
    isbn: int
    created_at: datetime
    updated_at: datetime