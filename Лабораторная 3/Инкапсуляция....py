from abc import ABC, abstractmethod

class Book(ABC):
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        """Возвращает название книги."""
        return self._name

    @property
    def author(self) -> str:
        """Возвращает автора книги."""
        return self._author

    @abstractmethod
    def __str__(self) -> str:
        """Возвращает строковое представление книги."""
        pass

    @abstractmethod
    def __repr__(self) -> str:
        """Возвращает представление книги для отладки."""
        pass
class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages  # Вызов свойства для валидации

    @property
    def pages(self) -> int:
        """Возвращает количество страниц."""
        return self._pages

    @pages.setter
    def pages(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом.")
        self._pages = value

    def __str__(self) -> str:
        return f"PaperBook(name='{self.name}', author='{self.author}', pages={self.pages})"

    def __repr__(self) -> str:
        return f"PaperBook({self.name!r}, {self.author!r}, {self.pages})"
class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration  # Вызов свойства для валидации

    @property
    def duration(self) -> float:
        """Возвращает продолжительность аудиокниги."""
        return self._duration

    @duration.setter
    def duration(self, value: float):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом.")
        self._duration = value

    def __str__(self) -> str:
        return f"AudioBook(name='{self.name}', author='{self.author}', duration={self.duration})"

    def __repr__(self) -> str:
        return f"AudioBook({self.name!r}, {self.author!r}, {self.duration})"
