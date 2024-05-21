# main.py
from models.book import Book
from repositories.book_repository import BookRepository

def main():
    book_repository = BookRepository()

    # Add books
    book_repository.add_book(Book("Python Crash Course", "Eric Matthes", "9781593279288"))
    book_repository.add_book(Book("Clean Code", "Robert C. Martin", "9780132350884"))
    book_repository.add_book(Book("Design Patterns", "Erich Gamma", "9780201633610"))

    # Get all books
    print("All books in the library:")
    for book in book_repository.get_all_books():
        print(book)

    # Get book by ISBN
    isbn = "9781593279288"
    book = book_repository.get_book_by_isbn(isbn)
    if book:
        print(f"\nBook with ISBN {isbn}: {book}")
    else:
        print(f"\nBook with ISBN {isbn} not found")

    # Remove book by ISBN
    isbn = "9780132350884"
    book_repository.remove_book_by_isbn(isbn)
    print(f"\nRemoved book with ISBN {isbn}")

    # Get all books after removal
    print("\nAll books in the library after removal:")
    for book in book_repository.get_all_books():
        print(book)

if __name__ == "__main__":
    main()
