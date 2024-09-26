import unittest
from src.library import Library
from src.book import Book

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book1 = Book("1234567890", "Test Book 1", "Test Author 1", 2023)
        self.book2 = Book("0987654321", "Test Book 2", "Test Author 2", 2022)

    def test_add_book(self):
        """Test adding a book to the library."""
        self.library.add_book(self.book1)
        self.assertIn(self.book1.isbn, self.library.books)

    def test_add_duplicate_book(self):
        """Test adding a duplicate book raises a ValueError."""
        self.library.add_book(self.book1)
        with self.assertRaises(ValueError):
            self.library.add_book(self.book1)

    def test_borrow_book(self):
        """Test borrowing an available book."""
        self.library.add_book(self.book1)
        self.library.borrow_book(self.book1.isbn)
        self.assertFalse(self.library.books[self.book1.isbn].is_available)

    def test_borrow_unavailable_book(self):
        """Test borrowing an unavailable book raises a ValueError."""
        self.library.add_book(self.book1)
        self.library.borrow_book(self.book1.isbn)
        with self.assertRaises(ValueError):
            self.library.borrow_book(self.book1.isbn)

    def test_borrow_nonexistent_book(self):
        """Test borrowing a non-existent book raises a ValueError."""
        with self.assertRaises(ValueError):
            self.library.borrow_book("nonexistent_isbn")

    def test_return_book(self):
        """Test returning a borrowed book."""
        self.library.add_book(self.book1)
        self.library.borrow_book(self.book1.isbn)
        self.library.return_book(self.book1.isbn)
        self.assertTrue(self.library.books[self.book1.isbn].is_available)

    def test_return_available_book(self):
        """Test returning an available book raises a ValueError."""
        self.library.add_book(self.book1)
        with self.assertRaises(ValueError):
            self.library.return_book(self.book1.isbn)

    def test_view_available_books(self):
        """Test viewing available books."""
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        self.library.borrow_book(self.book1.isbn)
        available_books = self.library.view_available_books()
        self.assertEqual(len(available_books), 1)
        self.assertEqual(available_books[0], self.book2)

if __name__ == '__main__':
    unittest.main()