import pytest
from lab06 import Book, EBook


def test_book_constructor():
    book = Book("The Hobbit", "J.R.R. Tolkien", 1937)
    assert book.title == "The Hobbit"
    assert book.author == "J.R.R. Tolkien"
    assert book.year == 1937


def test_book_str_method():
    book = Book("The Hobbit", "J.R.R. Tolkien", 1937)
    book_str = str(book)
    assert "The Hobbit" in book_str
    assert "J.R.R. Tolkien" in book_str
    assert "1937" in book_str


def test_book_get_age():
    book = Book("The Hobbit", "J.R.R. Tolkien", 1937)
    assert book.get_age() == 2025 - 1937


def test_book_get_age_recent():
    book = Book("Clean Code", "Robert Martin", 2008)
    assert book.get_age() == 2025 - 2008


def test_ebook_constructor():
    ebook = EBook("Dune", "Frank Herbert", 1965, 5)
    assert ebook.title == "Dune"
    assert ebook.author == "Frank Herbert"
    assert ebook.year == 1965
    assert ebook.file_size == 5


def test_ebook_str_method():
    ebook = EBook("Dune", "Frank Herbert", 1965, 5)
    ebook_str = str(ebook)
    assert "Dune" in ebook_str
    assert "Frank Herbert" in ebook_str
    assert "1965" in ebook_str
    assert "5" in ebook_str
    assert "MB" in ebook_str


def test_ebook_inherits_get_age():
    ebook = EBook("Dune", "Frank Herbert", 1965, 5)
    assert ebook.get_age() == 2025 - 1965


def test_ebook_with_different_file_size():
    small_ebook = EBook("Short Story", "Author Name", 2020, 2)
    large_ebook = EBook("Technical Manual", "Expert Author", 2018, 15)

    assert small_ebook.file_size == 2
    assert large_ebook.file_size == 15
    assert "2" in str(small_ebook) and "MB" in str(small_ebook)
    assert "15" in str(large_ebook) and "MB" in str(large_ebook)
