import doctest
from abc import ABC, abstractmethod
class Table(ABC):
    """
    Абстрактный класс, описывающий стол как физический объект.
    """
    def __init__(self, material: str, legs_count: int):
        """
        Создание объекта "Стол".
        :param material: Материал стола
        :param legs_count: Количество ножек
        Примеры:
        >>> class KitchenTable(Table):
        ...     def use(self): ...
        ...     def move(self, distance: float): ...
        >>> table = KitchenTable("wood", 4)
        """
        if not isinstance(material, str):
            raise TypeError("Материал должен быть строкой")
        if not isinstance(legs_count, int):
            raise TypeError("Количество ножек должно быть целым числом")
        if legs_count <= 0:
            raise ValueError("Количество ножек должно быть положительным")
        self.material: str = material
        self.legs_count: int = legs_count
    def use(self) -> None:
        """
        Использование стола по назначению.
        :return: None
        Примеры:
        >>> class TestTable(Table):
        ...     def use(self): ...
        ...     def move(self, distance: float): ...
        >>> TestTable("metal", 3).use()
        """
        ...
    def move(self, distance: float) -> None:
        """
        Перемещение стола.
        :param distance: Расстояние перемещения в метрах
        :return: None
        Примеры:
        >>> class TestTable(Table):
        ...     def use(self): ...
        ...     def move(self, distance: float): ...
        >>> TestTable("glass", 4).move(2.5)
        """
        if distance <= 0:
            raise ValueError("Расстояние должно быть положительным")
        ...
class Tree(ABC):
    """
    Абстрактный класс, описывающий дерево как живой организм.
    """
    def __init__(self, age: int, height: float):
        """
        Создание объекта "Дерево".
        :param age: Возраст дерева в годах
        :param height: Высота дерева в метрах
        Примеры:
        >>> class Oak(Tree):
        ...     def grow(self, years: int): ...
        ...     def shed_leaves(self): ...
        >>> tree = Oak(10, 3.5)
        """
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным")
        if height <= 0:
            raise ValueError("Высота должна быть положительной")
        self.age: int = age
        self.height: float = height
    def grow(self, years: int) -> None:
        """
        Рост дерева.

        :param years: Количество лет
        :return: None

        Примеры:
        >>> class TestTree(Tree):
        ...     def grow(self, years: int): ...
        ...     def shed_leaves(self): ...
        >>> TestTree(5, 2.0).grow(3)
        """
        if years <= 0:
            raise ValueError("Количество лет должно быть положительным")
        ...
    def shed_leaves(self) -> None:
        """
        Сбрасывание листьев.
        :return: None
        Примеры:
        >>> class TestTree(Tree):
        ...     def grow(self, years: int): ...
        ...     def shed_leaves(self): ...
        >>> TestTree(1, 1.2).shed_leaves()
        """
        ...
class SocialNetwork(ABC):
    """
    Абстрактный класс, описывающий социальную сеть.
    """
    def __init__(self, name: str, users_count: int):
        """
        Создание объекта "Социальная сеть".

        :param name: Название сети
        :param users_count: Количество пользователей

        Примеры:
        >>> class Network(SocialNetwork):
        ...     def register_user(self, username: str): ...
        ...     def send_message(self, sender: str, receiver: str): ...
        >>> sn = Network("ChatBook", 1000)
        """
        if not name:
            raise ValueError("Название не может быть пустым")
        if users_count < 0:
            raise ValueError("Количество пользователей не может быть отрицательным")
        self.name: str = name
        self.users_count: int = users_count
    def register_user(self, username: str) -> None:
        """
        Регистрация нового пользователя.
        :param username: Имя пользователя
        :return: None
        Примеры:
        >>> class TestSN(SocialNetwork):
        ...     def register_user(self, username: str): ...
        ...     def send_message(self, sender: str, receiver: str): ...
        >>> TestSN("TestNet", 0).register_user("admin")
        """
        if not username:
            raise ValueError("Имя пользователя не может быть пустым")
        ...
    def send_message(self, sender: str, receiver: str) -> None:
        """
        Отправка сообщения между пользователями.
        :param sender: Отправитель
        :param receiver: Получатель
        :return: None
        Примеры:
        >>> class TestSN(SocialNetwork):
        ...     def register_user(self, username: str): ...
        ...     def send_message(self, sender: str, receiver: str): ...
        >>> TestSN("TestNet", 2).send_message("alice", "bob")
        """
        ...
if __name__ == "__main__":
    doctest.testmod()