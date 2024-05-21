from typing import List
from .book import Book
from .book_repository import BookRepository

class InMemoryBookRepository(BookRepository):
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def get_book_by_title(self, title: str) -> Book:
        for book in self.books:
            if book.title == title:
                return book
        return None

    def get_all_books(self) -> List[Book]:
        return self.books
