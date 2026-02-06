class Book:
    """
    A simple Book class.

    Parameters
    ----------
    title : str
    author : str
    year : int
    """

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"\"{self.title}\" by {self.author} ({self.year})"

    def get_age(self):
        """
        Return the age of the book, assuming current year is 2025.
        """
        return 2025 - self.year


class EBook(Book):
    """
    An EBook that extends Book with file size (MB).

    Parameters
    ----------
    title : str
    author : str
    year : int
    file_size : int
    """

    def __init__(self, title, author, year, file_size):
        super().__init__(title, author, year)
        self.file_size = file_size

    def __str__(self):
        base = super().__str__()
        return f"{base} ({self.file_size} MB)"


if __name__ == "__main__":
    book = Book("The Hobbit", "J.R.R. Tolkien", 1937)
    print(book)
    print(book.get_age())

    ebook = EBook("Dune", "Frank Herbert", 1965, 5)
    print(ebook)
    print(ebook.get_age())
