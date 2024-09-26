# main.py

from src.library import Library
from src.book import Book

def main():
    library = Library()

    # Adding books
    book1 = Book("1234567890", "The Great Gatsby", "F. Scott Fitzgerald", 1925)
    book2 = Book("0987654321", "To Kill a Mockingbird", "Harper Lee", 1960)
    book3 = Book("1122334455", "1984", "George Orwell", 1949)

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    print("Available books:")
    for book in library.view_available_books():
        print(book)

    # Borrowing a book
    print("\nBorrowing 'The Great Gatsby'")
    library.borrow_book("1234567890")

    print("\nAvailable books after borrowing:")
    for book in library.view_available_books():
        print(book)

    # Returning a book
    print("\nReturning 'The Great Gatsby'")
    library.return_book("1234567890")

    print("\nAvailable books after returning:")
    for book in library.view_available_books():
        print(book)

if __name__ == "__main__":
    main()