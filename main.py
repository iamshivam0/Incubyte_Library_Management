# main.py

from src.library import Library
from src.book import Book

def print_menu():
    print("\nLibrary Management System")
    print("1. Add a book")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. View available books")
    print("5. Exit")

def get_book_info():
    isbn = input("Enter ISBN: ")
    title = input("Enter title: ")
    author = input("Enter author: ")
    year = int(input("Enter publication year: "))
    return Book(isbn, title, author, year)

def main():
    library = Library()

    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            try:
                book = get_book_info()
                library.add_book(book)
                print(f"Book '{book.title}' added successfully.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '2':
            isbn = input("Enter the ISBN of the book you want to borrow: ")
            try:
                library.borrow_book(isbn)
                print("Book borrowed successfully.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '3':
            isbn = input("Enter the ISBN of the book you want to return: ")
            try:
                library.return_book(isbn)
                print("Book returned successfully.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '4':
            available_books = library.view_available_books()
            if available_books:
                print("Available books:")
                for book in available_books:
                    print(book)
            else:
                print("No books available.")

        elif choice == '5':
            print("Thank you for using the Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()