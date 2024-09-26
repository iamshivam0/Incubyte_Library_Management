class Book:
    def __init__(self, isbn, title, author, publication_year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_available = True

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year}) - ISBN: {self.isbn}"
