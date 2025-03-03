class Book:
    def __init__(self, id_, name, pages):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f'Book(id_={self.id!r}, name={self.name!r}, pages={self.pages!r})'


class Library:
    def __init__(self, books=None):
        self.books = books if books is not None else []

    def get_next_book_id(self):
        # Создаем множество занятых идентификаторов
        used_ids = {book.id for book in self.books}
        # Начнем с 1 и будем искать первый доступный id
        next_id = 1
        while next_id in used_ids:
            next_id += 1
        return next_id

    def get_index_by_book_id(self, book_id):
        # Возвращает индекс книги по идентификатору
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


# Пример использования
library = Library()
print(library.get_next_book_id())  # Выведет: 1

# Создадим несколько книг
book1 = Book(id_=library.get_next_book_id(), name='test_name_1', pages=200)
library.books.append(book1)

print(library.get_next_book_id())  # Выведет: 2

book2 = Book(id_=library.get_next_book_id(), name='test_name_2', pages=300)
library.books.append(book2)

print(library.get_next_book_id())  # Выведет: 3

# Получим индекс книги по ее идентификатору
try:
    index = library.get_index_by_book_id(1)  # Существующая книга
    print(f"Индекс книги с id 1: {index}")  # Выведет: Индекс книги с id 1: 0
except ValueError as e:
    print(e)

try:
    index = library.get_index_by_book_id(3)  # Не существующая книга
    print(f"Индекс книги с id 3: {index}")
except ValueError as e:
    print(e)  # Выведет: Книги с запрашиваемым id не существует