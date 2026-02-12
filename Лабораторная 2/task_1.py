# TODO написать класс Book
class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Класс, описывающий книгу.
        :param id_: Идентификатор книги
        :param name: Название книги
        :param pages: Количество страниц
        """
        if not isinstance(id_, int):
            raise TypeError("id должен быть типа int")
        if not isinstance(name, str):
            raise TypeError("name должен быть типа str")
        if not isinstance(pages, int):
            raise TypeError("pages должен быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным")
        self.id = id_
        self.name = name
        self.pages = pages
    def __str__(self) -> str:
        """
        Строковое представление книги для пользователя.
        """
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """
        Валидное строковое представление объекта,
        по которому можно создать такой же экземпляр.
        """
        return f"Book(id_={self.id}, name={self.name!r}, pages={self.pages})"
BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]
if __name__ == '__main__':
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"])
        for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__
    print(list_books)  # проверяем метод __repr__
