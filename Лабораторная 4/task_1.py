class Vehicle:
    """
    Базовый класс транспортного средства.
    Описывает общие свойства и поведение любого транспортного средства.
    """
    def __init__(self, brand: str, max_speed: int):
        """
        Инициализация транспортного средства.
        :param brand: Марка транспортного средства
        :param max_speed: Максимальная скорость (км/ч)
        """
        if not isinstance(max_speed, int) or max_speed <= 0:
            raise ValueError("Максимальная скорость должна быть положительным целым числом")
        self.brand: str = brand
        self._max_speed: int = max_speed  # _max_speed инкапсулирован, чтобы запретить прямое изменение
    def drive(self, distance: float) -> None:
        """
        Движение транспортного средства.
        :param distance: Расстояние в километрах
        :return: None
        """
        if distance <= 0:
            raise ValueError("Расстояние должно быть положительным")
        # Реализация не обязательна
        ...
    def get_max_speed(self) -> int:
        """
        Возвращает максимальную скорость транспортного средства.
        :return: Максимальная скорость
        """
        return self._max_speed
    def __str__(self) -> str:
        return f"Транспортное средство марки {self.brand}"
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(brand={self.brand!r}, max_speed={self._max_speed})"
class Car(Vehicle):
    """
    Легковой автомобиль.
    Дочерний класс от Vehicle, расширяет функциональность
    и уточняет поведение некоторых методов.
    """
    def __init__(self, brand: str, max_speed: int, passengers: int):
        """
        Инициализация легкового автомобиля.
        Расширяет конструктор базового класса, добавляя количество пассажиров.
        :param brand: Марка автомобиля
        :param max_speed: Максимальная скорость
        :param passengers: Количество пассажиров
        """
        super().__init__(brand, max_speed)
        if passengers <= 0:
            raise ValueError("Количество пассажиров должно быть положительным")
        self.passengers: int = passengers
    def drive(self, distance: float) -> None:
        """
        Перегруженный метод движения автомобиля.
        Причина перегрузки:
        Легковой автомобиль перевозит пассажиров, поэтому логика движения
        может учитывать комфорт, остановки и безопасность пассажиров,
        чего нет в базовом транспортном средстве.
        :param distance: Расстояние в километрах
        :return: None
        """
        if distance <= 0:
            raise ValueError("Расстояние должно быть положительным")
        # Возможная логика движения автомобиля
        ...
    def honk(self) -> None:
        """
        Подача звукового сигнала.
        :return: None
        """
        ...
    def __str__(self) -> str:
        """
        Перегруженный __str__ для более детального описания автомобиля.
        """
        return f"Автомобиль {self.brand}, пассажиров: {self.passengers}"
    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"(brand={self.brand!r}, max_speed={self._max_speed}, passengers={self.passengers})"
        )
if __name__ == "__main__":
    vehicle = Vehicle("Generic", 120)
    car = Car("Toyota", 180, 5)
    print(vehicle)
    print(car)
    print(repr(vehicle))
    print(repr(car))