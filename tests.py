import pytest

from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_init_books_genre_no_data_empty(self, collector):

        assert collector.books_genre == {} and collector.favorites == []

    def test_init_favorites_no_data_empty(self, collector):

        assert collector.books_genre == {} and collector.favorites == []

    def test_init_genre_list_no_data_generated_list(self, collector):
        expected_genre_list = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

        assert collector.genre == expected_genre_list

    def test_init_genre_age_rating_list_no_data_generated_list(self, collector):
        expected_genre_age_rating = ['Ужасы', 'Детективы']

        assert collector.genre_age_rating == expected_genre_age_rating

    def test_add_new_book_name_lenght_less_40_book_added(self, collector):
        collector.add_new_book('Синий Трактор')

        assert collector.books_genre == {'Синий Трактор': ''}

    @pytest.mark.parametrize("name, expected_count", [
        ('Котёнок Гав', 1),  # Проверка при добавлении книги, которая уже есть в коллекции
        ('', 1),  # Проверка при пустом названии книги
        ('Барабулька' * 10, 1)  # Проверка при названии книги больше 40 символов длинной
    ])
    def test_add_new_book_incorrect_name_add_book_not_add(self, collector, name, expected_count):
        collector.add_new_book(name)
        collector.add_new_book('Котёнок Гав')

        assert collector.books_genre == {'Котёнок Гав': ''}

    def test_set_book_genre_book_and_genre_in_collectin_genre_added(self, collector):
        book, genre = ('Преступление и наказание', 'Детективы')
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)

        assert collector.books_genre == {book: genre}

    @pytest.mark.parametrize('name, genre', [
        ('Преступление и наказание', 'Скороговорки'),  # Жанр не существует
        ('Котёнок Гав', 'Мультфильмы'),  # Книга не существует
        ('', 'Детективы')  # Название книги не указано
    ])
    def test_set_book_genre_book_wrong_genre_request_genre_not_added(self, collector, name, genre):
        collector.add_new_book('Преступление и наказание')
        collector.set_book_genre(name, genre)

        assert collector.books_genre == {'Преступление и наказание': ''}

    def test_get_book_genre_one_book_genre_getted(self, collector):
        book, genre = ('Преступление и наказание', 'Детективы')
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)

        assert collector.get_book_genre(book) == 'Детективы'

    def test_get_books_with_specific_genre_exist_genre_books_shows(self, collector):
        books = [
            ['Звёздные Войны', 'Фантастика'],
            ['Доктор Кто', 'Фантастика'],
            ['Фунтик', 'Мультфильмы']
        ]
        for i in books:
            collector.add_new_book(i[0])
            collector.set_book_genre(i[0], i[1])

        assert collector.get_books_with_specific_genre('Фантастика') == ['Звёздные Войны', 'Доктор Кто']

    @pytest.mark.parametrize('genre', [
        ('Скороговорки'),  # Жанр не существует
        ('Комедии'),  # Книг жанра нет в коллекции
        ('')  # Жанр не указан
    ])
    def test_get_books_with_specific_genre_wrong_genre_empty_books_list(self, collector, genre):
        books = [
            ['Звёздные Войны', 'Фантастика'],
            ['Доктор Кто', 'Фантастика'],
            ['Фунтик', 'Мультфильмы']
        ]
        for i in books:
            collector.add_new_book(i[0])
            collector.set_book_genre(i[0], i[1])

        assert collector.get_books_with_specific_genre(genre) == []

    def test_get_books_genre_two_books_added_books_list_returned(self, collector):
        books = [
            ['Звёздные Войны', 'Фантастика'],
            ['Фунтик', 'Мультфильмы']
        ]
        for i in books:
            collector.add_new_book(i[0])
            collector.set_book_genre(i[0], i[1])

        assert collector.get_books_genre() == {'Звёздные Войны': 'Фантастика',
                                               'Фунтик': 'Мультфильмы'
                                               }

    def test_get_books_for_children_books_exist_shows_only_children_books(self, collector):
        books = [
            ['Звёздные Войны', 'Фантастика'],
            ['Доктор Кто', 'Фантастика'],
            ['Фунтик', 'Мультфильмы'],
            ['Кошмар на улице Вязов', 'Ужасы'],
            ['Мост', 'Детектив']
        ]
        for i in books:
            collector.add_new_book(i[0])
            collector.set_book_genre(i[0], i[1])

        assert collector.get_books_for_children() == ['Звёздные Войны', 'Доктор Кто', 'Фунтик']

    def test_add_book_in_favorites_two_books_add_book_added(self, collector):
        books = [
            ['Звёздные Войны', 'Фантастика'],
            ['Доктор Кто', 'Фантастика'],
            ['Фунтик', 'Мультфильмы'],
            ['Кошмар на улице Вязов', 'Ужасы'],
            ['Мост', 'Детектив']
        ]
        for i in books:
            collector.add_new_book(i[0])
            collector.set_book_genre(i[0], i[1])
        collector.add_book_in_favorites('Доктор Кто')
        collector.add_book_in_favorites('Фунтик')
        assert collector.favorites == ['Доктор Кто', 'Фунтик']

    def test_delete_book_from_favorites_two_books_added_one_deleted_one_book_left(self, collector):
        books = [
            ['Звёздные Войны', 'Фантастика'],
            ['Доктор Кто', 'Фантастика'],
            ['Фунтик', 'Мультфильмы'],
            ['Кошмар на улице Вязов', 'Ужасы'],
            ['Мост', 'Детектив']
        ]
        for i in books:
            collector.add_new_book(i[0])
            collector.set_book_genre(i[0], i[1])
        collector.add_book_in_favorites('Доктор Кто')
        collector.add_book_in_favorites('Фунтик')
        collector.delete_book_from_favorites('Доктор Кто')
        assert collector.favorites == ['Фунтик']

    def test_get_list_of_favorites_books_two_books_added_favorites_books_returned(self, collector):
        books = [
            ['Звёздные Войны', 'Фантастика'],
            ['Доктор Кто', 'Фантастика'],
            ['Фунтик', 'Мультфильмы'],
            ['Кошмар на улице Вязов', 'Ужасы'],
            ['Мост', 'Детектив']
        ]
        for i in books:
            collector.add_new_book(i[0])
            collector.set_book_genre(i[0], i[1])
        collector.add_book_in_favorites('Доктор Кто')
        collector.add_book_in_favorites('Фунтик')
        assert collector.get_list_of_favorites_books() == ['Доктор Кто', 'Фунтик']