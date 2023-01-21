import doctest


class Room:
    def __init__(self, side_a: float, side_b: float, side_c: float):
        """
        Создание и подготовка к работе объекта "Комната"
        :param side_a: Длина комнаты
        :param side_b: Ширина комнаты
        :param side_c: Высота комнаты
        Примеры:
        >>> room = Room(4.6, 5.0, 3.0)  # инициализация экземпляра класса
        """
        if not isinstance(side_a, (int, float)):
            raise TypeError("Длина комнаты должна быть типа int или float")
        if side_a <= 0:
            raise ValueError("Длина комнаты должна задаваться положительным числом")
        self.side_a = side_a

        if not isinstance(side_b, (int, float)):
            raise TypeError("Ширина комнаты должна быть типа int или float")
        if side_b <= 0:
            raise ValueError("Ширина комнаты должна задаваться положительным числом")
        self.side_b = side_b

        if not isinstance(side_c, (int, float)):
            raise TypeError("Высота комнаты должна быть типа int или float")
        if side_c <= 0:
            raise ValueError("Высота комнаты должна задаваться положительным числом")
        self.side_c = side_c

    def room_square(self) -> float:
        """
        Получить площадь комнаты.

        :return Выводит рассчитанный объем комнаты
        Примеры:
        >>> room = Room(4.6, 5.0, 3.0)
        >>> room.room_square()
        """
        ...
        return self.side_a * self.side_b

    def room_volume(self) -> float:
        """
        Получить объем комнаты.

        :return Выводит рассчитанный объем комнаты
        Примеры:
        >>> room = Room(4.6, 5.0, 3.0)
        >>> room.room_square()
        """
        ...
        return self.side_a * self.side_b * self.side_c

    def room_capacity(self, etalon=20) -> str:
        """
        Функция, определяющая свойство комнаты: большая или маленькая.
        :param etalon: сравнительная площадь

        :return Выводит сообщение "Комната отличная", если ее площадь >= эталонной или
                                  "Комната небольшая, но уютная", если площадь < эталонной
        Примеры:
        >>> room = Room(4.6, 5.0, 3.0)
        >>> room.room_capacity( 25)
        """

        if not isinstance(etalon, (int, float)):
            raise TypeError("Просьба ввести эталонную площадь в виде числового значения")
        if etalon < 0:
            raise ValueError("Введите положительное значение")

        ...

        return "Комната отличная" if self.room_volume >= etalon else "Комната небольшая, но уютная"

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации

    pass

import doctest
from datetime import date

class Car:
    def __init__(self, model: str, year: int, engine_capacity: float, color: str):
        """
        Объект Машины
        :param model: Марка машины
        :param year: Год выпуска
        :param engine_capacity: Мощность двигателя
        :param color: Цвет
        Примеры:
        >>> car = Car("BMW", 2012, 3.2, "black")  # инициализация экземпляра класса
        """
        self.model = model

        if not isinstance(year, (int)):
            raise TypeError("Год должен быть типа int")
        if year <= 1910 or year > date.today().year:
            raise ValueError("Неверно задан год выпуска")
        self.year = year

        if not isinstance(engine_capacity, (int, float)):
            raise TypeError("Объем двигателя должен быть int или float")
        if engine_capacity <= 0:
            raise ValueError("Объем двигателя должен задаваться положительным числом")
        self.engine_capacity = engine_capacity

        self.color = color

    def is_color_exists(self) -> bool:
        """
        Функция проверяет наличие модели требуемого цвета
        :return: Наличие модели указанного цвета
        Примеры:
        >>> car = Car("BMW", 2012, 3.2, "black")
        >>> car.is_color_exists()
        """
        ...

    def consumption(self, speed: float) -> float:
        """
        Расчет потребления бензина при заданной скорости
        :param speed: скорость
        :return рассчитанный расход бензина в литрах
        :raise ValueError: Если получилось деление на ноль
        Примеры:
        >>> car = Car("BMW", 2012, 3.2, "black")
        >>> car.consumption()
        """
        if not isinstance(speed, (int, float)):
            raise TypeError("Скорость должна быть типа int или float")
        if speed <= 0:
            raise ValueError("Скорость должна задаваться положительным числом")
        ...
        return ...

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации


    pass

import doctest

class Porridge:
    def __init__(self, groats: str, liquid: str, cook_time: float):
        """
        Объект Каша
        :param groats: Крупа
        :param liquid: На чем варить
        :param cook_time: Время варки (мин)

        Примеры:
        >>> porridge = Porridge("Овсянка", "Молоко", 5)
        """
        self.groats = groats

        if not isinstance(cook_time, (int, float)):
            raise TypeError("Укажите время варки в минутах")
        if cook_time <= 0:
            raise ValueError("Отрицательное время - это сильно")
        self.cook_time = cook_time

        if liquid not in ['Вода', 'Молоко']
            raise ValueError("Невкусно будет")
        self.liquid = liquid

    def cooking(self, portion: int) -> None:
        """
        Сварить кашу
        :param portion: количество порций
        :raise ValueError: если что-то пошло не так
        Примеры:
        >>> porridge = Porridge("Овсянка", "Молоко", 5)
        >>> porridge.cooking(3)
        """
        if not isinstance(portion, (int)):
            raise TypeError("Укажите целое количество порций")
        if cook_time <= 0:
            raise ValueError("Количество порций должно задаваться положительным числом")
        ..

        def sweety(self, spoon: int) -> None:
            """
        Посахарить кашу
        :param spoon: количество ложек сахара
        Примеры:
        >>> porridge = Porridge("Овсянка", "Молоко", 5)
        >>> porridge.sweety(1)
        """
            if not isinstance(spoon, (int)):
                raise TypeError("Укажите целое число ложек сахара"
                if spoon < 0:
                    raise ValueError("Количество ложек сахара не должно быть меньше 0")

    if __name__ == "__main__":
        doctest.testmod()  # тестирование примеров, которые находятся в документации
