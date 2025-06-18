class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        """Тест на добавление двух новых книг"""
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        books = collector.get_books_rating()
        assert 'Гордость и предубеждение и зомби' in books
        assert 'Что делать, если ваш кот хочет вас убить' in books

    def test_add_new_book_over_limit(self, collector):
        """Тест на добавление книги с длинным названием (больше 40 символов)"""
        long_name = 'К' * 41
        collector.add_new_book(long_name)
        books = collector.get_books_rating()
        assert long_name not in books

    def test_readd_book(self, collector):
        """Тест на повторное добавление одной и той же книги"""
        book_name = '1984'
        collector.add_new_book(book_name)
        collector.add_new_book(book_name)
        books = collector.get_books_rating()
        assert len(books) == 1

    def test_set_book_genre(self, collector):
        """Тест на установку жанра книги"""
        book_name = 'Моби Дик'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Приключения')
        assert collector.get_book_genre(book_name) == 'Приключения'

    def test_get_books_rating_empty(self, collector):
        """Тест на получение списка книг без добавленных книг"""
        assert collector.get_books_rating() == []

    def test_get_books_rating_non_empty(self, collector):
        """Тест на получение списка книг с добавленными книгами"""
        book_name = '1984'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Фантастика')
        books = collector.get_books_rating()
        assert book_name in books

    def test_get_books_with_specific_genre(self, collector):
        """Тест на получение списка книг с указанным жанром"""
        collector.add_new_book('Дама с собачкой')
        collector.set_book_genre('Дама с собачкой', 'Драма')
        collector.add_new_book('Как я провел лето')
        collector.set_book_genre('Как я провел лето', 'Приключения')
        assert collector.get_books_with_specific_genre('Драма') == ['Дама с собачкой']

    def test_get_books_for_children(self, collector):
        """Тест на получение списка книг, подходящих для детей"""
        collector.add_new_book('Кот в шляпе')
        collector.set_book_genre('Кот в шляпе', 'Сказка')
        books_for_children = collector.get_books_for_children()
        assert 'Кот в шляпе' in books_for_children

