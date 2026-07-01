class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        books_to_keep = []
        for book in self.books:
            if book.title or book.author == self.books:
                books_to_keep.pop(book)
        return books_to_keep

    def search_books(self, search_string):
        matches = []
        for book in self.books:
            if search_string.lower() in book.title or book.author:
                matches.append(book)
            return matches