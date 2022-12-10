import random
def get_random_password(len_=8) -> str:
    ...  # TODO написать функцию генерации случайных паролей

    upp_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    low_letters = 'abcdefghijklmnopqrstuvwxyz'
    num_letters = '0123456789'
    letter_list = [str for str in upp_letters+low_letters+num_letters]
    pwd = ''.join(random.sample (letter_list, len_))
    return pwd

print(get_random_password(8))
