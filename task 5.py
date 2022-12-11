import random
import string
def get_random_password(len_=8) -> str:
    ...  # TODO написать функцию генерации случайных паролей

    pwd = ''.join(random.sample(string.ascii_letters+string.digits, len_))

    return pwd

print(get_random_password(8))

