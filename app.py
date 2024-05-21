from bookstore.book import Book
from bookstore.in_memory_book_repository import InMemoryBookRepository
from bookstore.book_service import BookService

def main():
    repository = InMemoryBookRepository()
    service = BookService(repository)

    # Adding books
    service.add_book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
    service.add_book("To Kill a Mockingbird", "Harper Lee", "9780061120084")

    # Retrieving books
    print("All books:")
    for book in service.get_all_books():
        print(f"{book.title} by {book.author}")

    # Finding a book
    title = "The Great Gatsby"
    found_book = service.find_book_by_title(title)
    if found_book:
        print(f"Found {found_book.title} by {found_book.author}")
    else:
        print(f"Book with title {title} not found")

if __name__ == "__main__":
    main()
