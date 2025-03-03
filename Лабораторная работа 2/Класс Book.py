class Book:
    def __init__(self, id_, name, pages):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f'Book(id_={self.id!r}, name={self.name!r}, pages={self.pages!r})'


# Пример использования
book1 = Book(id_=1, name='test_name_1', pages=200)
book2 = Book(id_=2, name='test_name_2', pages=400)

print(str(book1))  # Выведет: Книга "test_name_1"
print(str(book2))  # Выведет: Книга "test_name_2"
print([book1, book2])  # Выведет список книг: [Book(id_=1, name='test_name_1', pages=200), Book(id_=2, name='test_name_2', pages=400)]