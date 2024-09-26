import unittest
from src.book import Book

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book("1234567890", "Test Book", "Test Author", 2023)

    def test_book_initialization(self):
        """Test proper initialization of a Book object."""
        self.assertEqual(self.book.isbn, "1234567890")
        self.assertEqual(self.book.title, "Test Book")
        self.assertEqual(self.book.author, "Test Author")
        self.assertEqual(self.book.publication_year, 2023)
        self.assertTrue(self.book.is_available)

    def test_book_str_representation(self):
        """Test the string representation of a Book object."""
        expected_str = "Test Book by Test Author (2023) - ISBN: 1234567890"
        self.assertEqual(str(self.book), expected_str)

if __name__ == '__main__':
    unittest.main()