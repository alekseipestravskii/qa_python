import pytest


class TestBooksCollector:

    def test_add_new_book(self, books_collector):
        books_collector.add_new_book("Книга 1")
        assert "Книга 1" in books_collector.books_genre
        assert books_collector.books_genre["Книга 1"] == ''

    def test_add_new_book_too_long_name(self, books_collector):
        books_collector.add_new_book("К" * 41)
        assert len(books_collector.books_genre) == 0

    def test_set_book_genre(self, books_collector):
        books_collector.add_new_book("Книга 2")
        books_collector.set_book_genre("Книга 2", "Фантастика")
        assert books_collector.get_book_genre("Книга 2") == "Фантастика"

    def test_get_book_genre(self, books_collector):
        books_collector.add_new_book("Книга 3")
        books_collector.set_book_genre("Книга 3", "Ужасы")
        assert books_collector.get_book_genre("Книга 3") == "Ужасы"

    def test_get_books_with_specific_genre(self, books_collector):
        books_collector.add_new_book("Книга 4")
        books_collector.set_book_genre("Книга 4", "Комедии")
        books_collector.add_new_book("Книга 5")
        books_collector.set_book_genre("Книга 5", "Комедии")
        assert books_collector.get_books_with_specific_genre("Комедии") == ["Книга 4", "Книга 5"]

    def test_books_for_children(self, books_collector):
        books_collector.add_new_book("Книга 6")
        books_collector.set_book_genre("Книга 6", "Ужасы")
        books_collector.add_new_book("Книга 7")
        books_collector.set_book_genre("Книга 7", "Детективы")
        books_collector.add_new_book("Книга 8")
        books_collector.set_book_genre("Книга 8", "Комедии")
        assert books_collector.get_books_for_children() == ["Книга 8"]

    def test_add_book_in_favorites(self, books_collector):
        books_collector.add_new_book("Книга 9")
        books_collector.add_book_in_favorites("Книга 9")
        assert "Книга 9" in books_collector.favorites

    def test_delete_book_from_favorites(self, books_collector):
        books_collector.add_new_book("Книга 10")
        books_collector.add_book_in_favorites("Книга 10")
        books_collector.delete_book_from_favorites("Книга 10")
        assert "Книга 10" not in books_collector.favorites

    def test_get_list_of_favorites_books(self, books_collector):
        books_collector.add_new_book("Книга 11")
        books_collector.add_book_in_favorites("Книга 11")
        assert books_collector.get_list_of_favorites_books() == ["Книга 11"]

    @pytest.mark.parametrize("book_name,expected", [
        ("Книга 12", ''),
        ("", ''),
        ("К" * 41, ''),
    ])
    def test_add_new_book_various_names(self, books_collector, book_name, expected):
        books_collector.add_new_book(book_name)
        assert books_collector.books_genre.get(book_name) == expected

    def test_get_books_genre(self, books_collector):
        """Тест на получение всех книг и их жанров"""
        books_collector.add_new_book("Книга 13")
        books_collector.set_book_genre("Книга 13", "Фантастика")
        assert books_collector.get_books_genre() == {"Книга 13": "Фантастика"}