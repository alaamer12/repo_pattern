from abc import ABC, abstractmethod
from typing import List
from .book import Book

class BookRepository(ABC):
    @abstractmethod
    def add_book(self, book: Book):
        pass

    @abstractmethod
    def get_book_by_title(self, title: str) -> Book:
        pass

    @abstractmethod
    def get_all_books(self) -> List[Book]:
        pass
