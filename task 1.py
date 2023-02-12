
import doctest


class Furniture:
    """
    Базовый класс "Мягкая мебель".
    :param color: Цвет
    :param material: Материал
    :param width: Ширина
    
    Примеры:
    >>> Furniture = Furniture(color = "красный", material = "кожзам", width = 0.8) # инициализация экземпляра класса
  
    """
   
    def __init__(self, color: str,  material: str, width: float):
    
        if not isinstance(color, str):
            raise TypeError('Цвет должен быть типа str.') 

        if not isinstance(material, str):
            raise TypeError('материал должен быть типа str.')  
        
        if not isinstance(width, float):
            raise TypeError('Ширина должна быть типа str.') 
        if width < 0:
            raise ValueError('Ширина не может быть меньше 0')     

        self._color = color
        self._material = material
        self._width = width

    @property
    def color(self) -> str:
        return self._color
   
    @property
    def materail(self) -> str:
        return self._material

    @property
    def width(self) -> float:
        return self._width

    def __str__(self):
        return f"Мягкая мебель: цвет {self._color} материал {self._material} "

    def __repr__(self):
        return f"{self.__class__.__name__}(color= {self._color!r}, material={self._material!r}, width={self._width})"

    def comfort_sit(self) -> str:
        """
        Функция, которая вычисляет, удобно ли сидеть на данной мебели.
        >>> Furniture = Furniture(color = "красный", material = "кожзам", width = 0.8) # инициализация экземпляра класса
        >>> Furniture.comfort_sit()
        'Комфортно сидеть'
        """ 
        return f"Комфортно сидеть" if self._width <= 0.8 else f"Нужны дополнителеные подушки"
        
 
 
class Sofa (Furniture):
    
    """
    Подкласс "Диваны".
    :param color: Цвет
    :param material: Материал
    :param width: Ширина
    :param mechanism: Тип механизма (раскладной, не раскладной)
    :param length: Длина
    
    Примеры:
    >>> Sofa = Sofa(color = "красный", material = "кожаный", width = 0.8, mechanism = "дельфин", length = 2) # инициализация экземпляра подкласса
  
    """

    def __init__(self, color: str, material: str, width: float, mechanism: str, length: float):
        super().__init__(color, material, width)


        if not isinstance(length, (int,float)):
            raise TypeError('Длина должна быть типа число') 
        if length < 0:
            raise ValueError('Длина не может быть меньше 0')
            
        if not isinstance(mechanism, str):
            raise TypeError('Механизм должен быть типа str.')         

        self._length = length
        self._mechanism = mechanism

    @property
    def length(self) -> float:
        return self._length

    @property
    def mechanism(self) -> str:
        return self._mechanism
    
    
    def __str__(self):
        return f"{self._color} {self._material} диван длиной {self._length} м"

    def __repr__(self):
        return f"{self.__class__.__name__}(color= {self._color!r}, material={self._material!r}, width={self._width}, mechanism={self._mechanism!r}, length={self._length})"

    def comfort_lay(self) -> str:
        """
        Функция, которая вычисляет, удобно ли лежать на данном диване.
        >>> Sofa = Sofa(color = "красный", material = "кожаный", width = 0.8, mechanism = "дельфин", length = 2) # инициализация экземпляра подкласса
        >>> Sofa.comfort_lay()
        'Комфортно лежать'
        """
        
        return f"Комфортно лежать" if self._length >= 1.8 else f"Нужно подгибать ноги"
       



class corner_sofa(Sofa):
    
    """
    Подкласс "Угловые диваны".
    :param color: Цвет
    :param material: Материал
    :param width: Ширина
    :param mechanism: Тип механизма (раскладной, не раскладной)
    :param length: Длина
    :corner: Угол поворота дивана вправо или влево
    
    Примеры:
    >>> corner_sofa = corner_sofa(color = "красный", material = "кожаный", width = 0.8, mechanism = "дельфин", length = 2, corner = "правый") # инициализация экземпляра подкласса
  
    """
    
    def __init__(self, color: str, material: str, width: float, mechanism: str, length: float, corner: str):
        super().__init__(color, material, width, mechanism, length)
        self._corner = corner
    
    @property
    def corner(self) -> str:
        return self._corner

    def __repr__(self):
        return f"{self.__class__.__name__}(color= {self._color!r}, material={self._material!r}, width={self._width},mechanism={self._mechanism!r}, length={self._length}, corner={self._corner!r})"


class Armchair (Furniture):
    
    """
    Подкласс "Кресла".
    :param color: Цвет
    :param material: Материал
    :param width: Ширина
    :param armrest: Наличие подлокотника 
    
    Примеры:
    >>> Armchair = Armchair(color = "красный", material = "кожзам", width = 0.8,armrest = False) # инициализация экземпляра подкласса
  
    """
    
    def __init__(self, color: str,  material: str, width: float, armrest: bool):
        super().__init__(color, material, width)

        self._armrest = armrest
        
        if not isinstance(armrest, bool):
            raise TypeError('Наличие подклокотников задается в виде "true", "false".')         

    @property
    def armrest(self) -> bool:
        return self._armrest
    
    
    def __str__(self):
        return f"{self._color} {self._material} кресло с подлокотниками" if {self._armrest} == True else f"{self._color} {self._material} кресло" 

    def __repr__(self):
        return f"{self.__class__.__name__}(color= {self._color!r}, material={self._material!r}, width={self._width}, armrest={self._armrest!r})"

  

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    

