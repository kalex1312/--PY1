
import random

def get_unique_list_numbers() -> list[int]:
    ...  # TODO написать функцию для получения списка уникальных целых чисел

    list_numbers = []
    while (len(list_numbers)) < 15:
       random_int = random.randint(-10, 10)
       if random_int not in list_numbers:
           list_numbers.append(random_int)

    # list_numbers = random.sample (range(-10,10),15) вариант 2
    return list_numbers



list_unique_numbers = get_unique_list_numbers()
print("результат:", list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
