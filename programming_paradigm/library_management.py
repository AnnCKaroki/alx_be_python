class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title.lower() == title.lower():
                if not book._is_checked_out:
                    book._is_checked_out = True
                    return

    def return_book(self, title):
        for book in self._books:
            if book.title.lower() == title.lower():
                if book._is_checked_out:
                    book._is_checked_out = False
                    return

    def list_available_books(self):
        available = []
        for book in self._books:
            if not book._is_checked_out:
                available.append(book.title)
        return available
