# TODO написать класс Book
# TODO написать класс Library
class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Класс, описывающий книгу.

        :param id_: Идентификатор книги
        :param name: Название книги
        :param pages: Количество страниц
        """
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным")

        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f"Book(id_={self.id}, name={self.name!r}, pages={self.pages})"


class Library:
    def __init__(self, books: list[Book] | None = None):
        """
        Класс, описывающий библиотеку.

        :param books: Список книг
        """
        # важно не использовать изменяемый объект как аргумент по умолчанию
        self.books: list[Book] = books if books is not None else []

    def get_next_book_id(self) -> int:
        """
        Возвращает следующий идентификатор книги.

        :return: int
        """
        if not self.books:
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Возвращает индекс книги по её идентификатору.

        :param book_id: Идентификатор книги
        :return: Индекс книги в списке

        :raise ValueError: Если книги с таким id не существует
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index

        raise ValueError("Книги с запрашиваемым id не существует")


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
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # 1

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"])
        for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)
    print(library_with_books.get_next_book_id())  # 3

    print(library_with_books.get_index_by_book_id(1))  # 0
