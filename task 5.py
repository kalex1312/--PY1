import random
import string
def get_random_password(len_=8) -> str:
    ...  # TODO написать функцию генерации случайных паролей

    letter_list = [str for str in string.ascii_letters+string.digits]
    pwd = ''.join(random.sample (letter_list, len_))
    return pwd

print(get_random_password(8))

