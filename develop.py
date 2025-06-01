

class BooksCollector:
    def __init__(self):
        self.books_genre = {}
        self.favorites = []
        self.genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        self.genre_age_rating = ['Ужасы', 'Детективы']

    def add_new_book(self, name):
        if not self.books_genre.get(name) and 0 < len(name) < 41:
            self.books_genre[name] = ''

    def set_book_genre(self, name, genre):
        if name in self.books_genre and genre in self.genre:
            self.books_genre[name] = genre

    def get_book_genre(self, name):
        return self.books_genre.get(name)

    def get_books_with_specific_genre(self, genre):
        books_with_specific_genre = []
        if self.books_genre and genre in self.genre:
            for name, book_genre in self.books_genre.items():
                if book_genre == genre:
                    books_with_specific_genre.append(name)
        return books_with_specific_genre

    def get_books_genre(self):
        return self.books_genre

    def get_books_for_children(self):
        books_for_children = []
        for name, genre in self.books_genre.items():
            if genre not in self.genre_age_rating and genre in self.genre:
                books_for_children.append(name)
        return books_for_children

    def add_book_in_favorites(self, name):
        if name in self.books_genre:
            if name not in self.favorites:
                self.favorites.append(name)

    def delete_book_from_favorites(self, name):
        if name in self.favorites:
            self.favorites.remove(name)

    def get_list_of_favorites_books(self):
        return self.favorites


class TestBooksCollector:

    @pytest.fixture
    def books_collector(self):
        """Фикстура, создающая новый экземпляр BooksCollector для каждого теста."""
        return BooksCollector()

    def test_add_new_book(self, books_collector):
        # Проверяем добавление новой книги
        books_collector.add_new_book("Книга 1")
        assert "Книга 1" in books_collector.books_genre
        assert books_collector.books_genre["Книга 1"] == ''

    def test_add_new_book_too_long_name(self, books_collector):
        # Проверяем, что книга с длинным названием не добавляется
        books_collector.add_new_book("К" * 41)
        assert len(books_collector.books_genre) == 0

    def test_set_book_genre(self, books_collector):
        # Проверяем установку жанра книги
        books_collector.add_new_book("Книга 2")
        books_collector.set_book_genre("Книга 2", "Фантастика")
        assert books_collector.get_book_genre("Книга 2") == "Фантастика"

    def test_get_book_genre(self, books_collector):
        # Проверяем получение жанра книги
        books_collector.add_new_book("Книга 3")
        books_collector.set_book_genre("Книга 3", "Ужасы")
        assert books_collector.get_book_genre("Книга 3") == "Ужасы"

    def test_get_books_with_specific_genre(self, books_collector):
        # Проверяем получение списка книг с указанным жанром
        books_collector.add_new_book("Книга 4")
        books_collector.set_book_genre("Книга 4", "Комедии")
        books_collector.add_new_book("Книга 5")
        books_collector.set_book_genre("Книга 5", "Комедии")
        assert books_collector.get_books_with_specific_genre("Комедии") == ["Книга 4", "Книга 5"]

    def test_books_for_children(self, books_collector):
        # Проверяем, что книги с рейтингом не добавляются в книги для детей
        books_collector.add_new_book("Книга 6")
        books_collector.set_book_genre("Книга 6", "Ужасы")
        books_collector.add_new_book("Книга 7")
        books_collector.set_book_genre("Книга 7", "Детективы")
        books_collector.add_new_book("Книга 8")
        books_collector.set_book_genre("Книга 8", "Комедии")
        assert books_collector.get_books_for_children() == ["Книга 8"]

    def test_add_book_in_favorites(self, books_collector):
        # Проверяем добавление книги в избранное
        books_collector.add_new_book("Книга 9")
        books_collector.set_book_genre("Книга 9", "Фантастика")
        books_collector.add_book_in_favorites("Книга 9")
        assert "Книга 9" in books_collector.favorites

    def test_delete_book_from_favorites(self, books_collector):
        # Проверяем удаление книги из избранного
        books_collector.add_new_book("Книга 10")
        books_collector.set_book_genre("Книга 10", "Фантастика")
        books_collector.add_book_in_favorites("Книга 10")
        books_collector.delete_book_from_favorites("Книга 10")
        assert "Книга 10" not in books_collector.favorites

    def test_get_list_of_favorites_books(self, books_collector):
        # Проверка списка избранных книг
        books_collector.add_new_book("Книга 11")
        books_collector.set_book_genre("Книга 11", "Фантастика")
        books_collector.add_book_in_favorites("Книга 11")
        assert books_collector.get_list_of_favorites_books() == ["Книга 11"]

    @pytest.mark.parametrize("book_name,expected", [
        ("Книга 12", ''),
        ("", ''),  # Пустое имя не добавляется
        ("К" * 41, ''),
    ])
    def test_add_new_book_various_names(self, books_collector, book_name, expected):
        # Проверяем добавление книг с различными названиями
        books_collector.add_new_book(book_name)
        assert books_collector.books_genre.get(book_name) == expected