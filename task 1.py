
class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author


    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)

        self.pages = pages

    def __str__(self):
        return f"Бумажная книга {self.name}. Автор {self.author}. {self.pages} страниц"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, pages: int) -> None:

        if not isinstance(pages, int):
            raise TypeError('Число страниц в книге должно быть целым числом.')
        if pages <= 0:
            raise ValueError('Число страниц должно быть положительным.')
        self._pages = pages



class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)

        self.duration = duration

    def __str__(self):
        return f" Электронная книга {self.name}. Автор {self.author}. Длительность {self.duration} часов."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, duration: float) -> None:

        if not isinstance(duration, (int ,float)):
            raise TypeError('Длительность должна быть числом.')
        if duration < 0:
            raise ValueError('Длительность должны быть положительна.')
        self._duration = duration



