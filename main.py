import pytest


class TestBooksCollector:
    # 1-------------------------------------------------------------------------V
    def test_add_new_book_add_two_books_success(self, collector):
        collector.add_new_book('First book')
        collector.add_new_book('Second book')
        assert len(collector.get_books_genre()) == 2

    # 2--------------------------------------------------------------------------
    @pytest.mark.parametrize('name', ['', '123456789 123456789 123456789 123456789 !'])
    def test_add_new_book_add_incorrect_name_failed(self, collector, name):
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 0

    # 3--------------------------------------------------------------------------
    @pytest.mark.parametrize(
        'name, genre',
        [
            ['First book', 'incorrect genre'],
            ['First book', '']
        ]
    )
    def test_set_book_genre_incorrect_genre_failed(self, collector, name, genre):
        collector.add_new_book('First book')
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == ''

    # 4--------------------------------------------------------------------------
    @pytest.mark.parametrize(
        'name, genre',
        [
            ['First book', 'Фантастика'],
            ['Second book', None]
        ]
    )
    def test_get_book_genre_success(self, collector, name, genre):
        collector.add_new_book('First book')
        collector.set_book_genre('First book', 'Фантастика')
        assert collector.get_book_genre(name) == genre

    # 5--------------------------------------------------------------------------
    def test_get_books_with_specific_genre_add_dict_success(self, collector):
        books = {
            'First book': 'Ужасы',
            'Second book': 'Фантастика',
            'Third book': 'Ужасы',
            'Fourth book': 'Мультфильмы',
            'Fifth book': 'Нуар'
        }
        for name, genre in books.items():
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)
        assert ['First book', 'Third book'] == collector.get_books_with_specific_genre('Ужасы')

    # 6--------------------------------------------------------------------------
    def test_get_books_with_specific_genre_wrong_genre_failed(self, collector):
        collector.add_new_book('First book')
        collector.set_book_genre('First book', 'Ужасы')
        assert len(collector.get_books_with_specific_genre('Нуар')) == 0

    # 7--------------------------------------------------------------------------
    def test_get_books_genre_success(self, collector):
        books = {
            'First book': 'Ужасы',
            'Second book': 'Фантастика',
            'Third book': 'Ужасы'
        }
        for name, genre in books.items():
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)
        assert books == collector.get_books_genre()

    # 8--------------------------------------------------------------------------
    def test_get_books_for_children_success(self, collector):
        books = {'Adult book1': 'Ужасы',
                 'Adult book2': 'Детективы',
                 'Children book': 'Мультфильмы'}
        for name, genre in books.items():
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)
        assert collector.get_books_for_children() == ['Children book']

    # 9--------------------------------------------------------------------------
    def test_add_book_in_favorites_correct_name_success(self, collector):
        collector.add_new_book('First book')
        collector.add_book_in_favorites('First book')

        assert len(collector.get_list_of_favorites_books()) == 1

    # 10--------------------------------------------------------------------------
    @pytest.mark.parametrize('name', ['First book', 'Second book'])
    def test_add_book_in_favorites_incorrect_failed(self, collector, name):
        collector.add_new_book('First book')
        collector.add_book_in_favorites('First book')
        collector.add_book_in_favorites(name)
        assert len(collector.get_list_of_favorites_books()) == 1

    # 11--------------------------------------------------------------------------
    def test_delete_book_from_favorites_one_book_success(self, collector):
        collector.add_new_book('First book')
        collector.add_book_in_favorites('First book')
        collector.delete_book_from_favorites('First book')
        assert len(collector.get_list_of_favorites_books()) == 0

    # 12--------------------------------------------------------------------------
    def test_delete_book_from_favorites_wrong_book_failed(self, collector):
        collector.add_new_book('First book')
        collector.add_book_in_favorites('First book')
        collector.delete_book_from_favorites('Second book')
        assert len(collector.get_list_of_favorites_books()) == 1

    # 13--------------------------------------------------------------------------
    def test_get_list_of_favorites_books_success(self, collector):
        collector.add_new_book('First book')
        collector.add_book_in_favorites('First book')
        collector.add_new_book('Second book')
        assert collector.get_list_of_favorites_books() == ['First book']