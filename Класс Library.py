
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

class Book:
    def __init__(self, id: int, name: str, pages: int):

        """
        Создание и подготовка к работе объекта "Книга"
        :param id_: Идентификатор книги
        :param name_: Название книги
        :param pages_: Количество страниц в книге
        """

        if not isinstance(id, (int)):
            raise TypeError("Идентификатор книги должен быть типа int")
        if id <= 0:
            raise ValueError("Идентификтаор должен задаваться положительным числом")
        self.id = id

        self.name = name

        if not isinstance(pages, (int)):
            raise TypeError("Кол-во страниц должны быть типа int")
        if pages <= 0:
            raise ValueError("Кол-во страниц должны задаваться положительным числом")
        self.pages = pages


class Library:
    def __init__(self, books:list[Book]=[]):

        """
        Создание и подготовка к работе объекта "Библиотека"
        :param books_: Список книг
        """

        if not isinstance(books, list):
            raise TypeError("Параметр books должен быть задан списком")
        self.books = books

    def get_next_book_id(self) -> int:
        return 1 if self.books == [] else len(self.books) + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        if not isinstance(book_id, int):
            raise TypeError("Идентификатор книги должен быть типа int")

        for i, current_book in enumerate(self.books):
            if current_book.id == book_id:
                return i
        raise ValueError('Книги с запрашиваемым id не существует')


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]

    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1


