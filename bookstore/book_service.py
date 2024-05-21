from .book import Book
from .book_repository import BookRepository

class BookService:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.repository.add_book(book)

    def find_book_by_title(self, title):
        return self.repository.get_book_by_title(title)

    def get_all_books(self):
        return self.repository.get_all_books()
