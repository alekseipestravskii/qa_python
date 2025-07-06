import pytest
from main import BooksCollector


@pytest.fixture # создаём объект коллекции
def collector():
    collector = BooksCollector()
    return collector