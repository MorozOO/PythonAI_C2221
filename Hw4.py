# Simulation of a Library System

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False

    def check_out(self):
        self.is_checked_out = True

    def return_book(self):
        self.is_checked_out = False


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def check_out_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_checked_out:
                book.check_out()
                return f"{title} has been checked out."
        return f"{title} is not available."

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.is_checked_out:
                book.return_book()
                return f"{title} has been returned."
        return f"{title} was not checked out."
