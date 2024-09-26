
from src.book import Book

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        if not isinstance(book, Book):
            raise ValueError("Only Book objects can be added to the library")
        if book.isbn in self.books:
            raise ValueError(f"Book with ISBN {book.isbn} already exists in the library")
        self.books[book.isbn] = book

    def borrow_book(self, isbn):
        if isbn not in self.books:
            raise ValueError(f"Book with ISBN {isbn} not found in the library")
        book = self.books[isbn]
        if not book.is_available:
            raise ValueError(f"Book with ISBN {isbn} is not available for borrowing")
        book.is_available = False

    def return_book(self, isbn):
        if isbn not in self.books:
            raise ValueError(f"Book with ISBN {isbn} not found in the library")
        book = self.books[isbn]
        if book.is_available:
            raise ValueError(f"Book with ISBN {isbn} is already in the library")
        book.is_available = True

    def view_available_books(self):
        return [book for book in self.books.values() if book.is_available]