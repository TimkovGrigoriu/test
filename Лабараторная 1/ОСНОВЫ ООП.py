from abc import ABC, abstractmethod

class Furniture(ABC):
    def __init__(self, material: str, color: str, height: float):
        """
        Конструктор класса Furniture.

        :param material: Материал, из которого изготовлена мебель. Не может быть пустым.
        :param color: Цвет мебели. Не может быть пустым.
        :param height: Высота мебели в сантиметрах. Должна быть положительным числом.
        """
        if not material:
            raise ValueError("Материал не может быть пустым.")
        if not color:
            raise ValueError("Цвет не может быть пустым.")
        if height <= 0:
            raise ValueError("Высота должна быть положительным числом.")

        self.material = material
        self.color = color
        self.height = height

    @abstractmethod
    def assemble(self) -> None:
        """Собрать мебель."""
        ...

    @abstractmethod
    def disassemble(self) -> None:
        """Разобрать мебель."""
        ...

    @abstractmethod
    def paint(self, new_color: str) -> None:
        """
        Покрасить мебель в новый цвет.

        :param new_color: Новый цвет мебели.
        """
        ...
class Plant(ABC):
    def __init__(self, species: str, age: int, height: float):
        """
        Конструктор класса Plant.

        :param species: Вид растения. Не может быть пустым.
        :param age: Возраст растения в годах. Должен быть неотрицательным числом.
        :param height: Высота растения в сантиметрах. Должна быть положительным числом.
        """
        if not species:
            raise ValueError("Вид растения не может быть пустым.")
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным.")
        if height <= 0:
            raise ValueError("Высота должна быть положительным числом.")

        self.species = species
        self.age = age
        self.height = height

    @abstractmethod
    def water(self, amount: float) -> None:
        """
        Полить растение.

        :param amount: Количество воды в миллилитрах.
        """
        ...

    @abstractmethod
    def prune(self) -> None:
        """Обрезать растение."""
        ...

    @abstractmethod
    def fertilize(self, fertilizer_type: str) -> None:
        """
        Удобрить растение.

        :param fertilizer_type: Тип удобрения.
        """
        ...
class SocialMedia(ABC):
    def __init__(self, platform_name: str, user_count: int):
        """
        Конструктор класса SocialMedia.

        :param platform_name: Название платформы. Не может быть пустым.
        :param user_count: Количество пользователей. Должно быть неотрицательным числом.
        """
        if not platform_name:
            raise ValueError("Название платформы не может быть пустым.")
        if user_count < 0:
            raise ValueError("Количество пользователей не может быть отрицательным.")

        self.platform_name = platform_name
        self.user_count = user_count

    @abstractmethod
    def post_content(self, content: str) -> None:
        """
        Опубликовать контент на платформе.

        :param content: Содержимое для публикации.
        """
        ...

    @abstractmethod
    def delete_account(self, user_id: str) -> None:
        """
        Удалить аккаунт пользователя.

        :param user_id: Идентификатор пользователя.
        """
        ...

    @abstractmethod
    def analyze_trends(self) -> dict:
        """
        Проанализировать текущие тренды.

        :return: Словарь с данными о трендах.
        """
        ...
