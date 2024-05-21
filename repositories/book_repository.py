# repositories/book_repository.py
from models.book import Book

class BookRepository:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def remove_book_by_isbn(self, isbn):
        self.books = [book for book in self.books if book.isbn != isbn]

    def get_all_books(self):
        return self.books
