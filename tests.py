import pytest
from main import BooksCollector



class TestBooksCollector:

    @pytest.fixture
    def collector(self):
        """Создает новый экземпляр BooksCollector для каждого теста."""
        return BooksCollector()


    def test_add_new_book_add_two_books(self, collector):

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')


        assert len(collector.get_books_rating()) == 2



    def test_add_new_book_over_limit(self, collector):
        """Тест на добавление книги с длинным названием (больше 40 символов)"""
        long_name = 'К' * 41
        collector.add_new_book(long_name)
        assert len(collector.get_books_rating()) == 0

    def test_readd_book(self, collector):
        """Тест на повторное добавление одной и той же книги"""
        book_name = '1984'
        collector.add_new_book(book_name)
        collector.add_new_book(book_name)

        assert len(collector.get_books_rating()) == 1

    def test_set_book_genre(self, collector):
        """Тест на установку жанра книги"""
        book_name = 'Моби Дик'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Приключения')

        assert collector.get_book_genre(book_name) == 'Приключения'

    def test_books_for_children(self, collector):
        """Тест на получение списка книг, подходящих для детей"""
        collector.add_new_book('Кот в шляпе')
        collector.set_book_genre('Кот в шляпе', 'Детская литература')

        assert 'Кот в шляпе' in collector.get_books_for_children()  