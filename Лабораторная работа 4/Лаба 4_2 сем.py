class Vehicle:
    """
    Базовый класс для всех транспортных средств.
    """

    def __init__(self, make: str, model: str, year: int) -> None:
        """
        Инициализация транспортного средства.

        :param make: Производитель транспортного средства.
        :param model: Модель транспортного средства.
        :param year: Год выпуска транспортного средства.
        """
        self._make = make  # Инкапсуляция: атрибуты не должны быть доступны напрямую
        self._model = model
        self._year = year

    def __str__(self) -> str:
        """Возвращает строковое представление транспортного средства."""
        return f"{self._year} {self._make} {self._model}"

    def __repr__(self) -> str:
        """Возвращает формальное строковое представление транспортного средства."""
        return f"Vehicle(make='{self._make}', model='{self._model}', year={self._year})"

    def start_engine(self) -> str:
        """Запускает двигатель транспортного средства."""
        return "Двигатель запущен."


class Car(Vehicle):
    """
    Класс для легковых автомобилей, наследует от Vehicle.
    """

    def __init__(self, make: str, model: str, year: int, doors: int) -> None:
        """
        Инициализация легкового автомобиля.

        :param make: Производитель легкового автомобиля.
        :param model: Модель легкового автомобиля.
        :param year: Год выпуска легкового автомобиля.
        :param doors: Количество дверей в легковом автомобиле.
        """
        super().__init__(make, model, year)  # Вызов конструктора базового класса
        self._doors = doors  # Инкапсуляция: атрибут не должен быть доступен напрямую

    def __str__(self) -> str:
        """Возвращает строковое представление легкового автомобиля."""
        return f"{super().__str__()} с {self._doors} дверями"

    def __repr__(self) -> str:
        """Возвращает формальное строковое представление легкового автомобиля."""
        return f"Car(make='{self._make}', model='{self._model}', year={self._year}, doors={self._doors})"

    def start_engine(self) -> str:
        """
        Запускает двигатель легкового автомобиля.

        Переопределяет метод базового класса, чтобы добавить дополнительное сообщение.
        """
        return f"{super().start_engine()} Легковой автомобиль готов к поездке."


class Truck(Vehicle):
    """
    Класс для грузовых автомобилей, наследует от Vehicle.
    """

    def __init__(self, make: str, model: str, year: int, capacity: float) -> None:
        """
        Инициализация грузового автомобиля.

        :param make: Производитель грузового автомобиля.
        :param model: Модель грузового автомобиля.
        :param year: Год выпуска грузового автомобиля.
        :param capacity: Грузоподъемность грузового автомобиля в тоннах.
        """
        super().__init__(make, model, year)  # Вызов конструктора базового класса
        self._capacity = capacity  # Инкапсуляция: атрибут не должен быть доступен напрямую

    def __str__(self) -> str:
        """Возвращает строковое представление грузового автомобиля."""
        return f"{super().__str__()} с грузоподъемностью {self._capacity} тонн"

    def __repr__(self) -> str:
        """Возвращает формальное строковое представление грузового автомобиля."""
        return f"Truck(make='{self._make}', model='{self._model}', year={self._year}, capacity={self._capacity})"

    def start_engine(self) -> str:
        """
        Запускает двигатель грузового автомобиля.

        Переопределяет метод базового класса, чтобы добавить дополнительное сообщение.
        """
        return f"{super().start_engine()} Грузовой автомобиль готов к работе."
