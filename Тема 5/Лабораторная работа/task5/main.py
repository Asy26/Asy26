from random import sample
import string

def get_random_password() -> str:

          # TODO написать функцию генерации случайных паролей
    a = string.ascii_lowercase
    b = string.ascii_uppercase
    c = string.digits
    d = (a + b + c)
    password = ''.join(sample(d, 8))
    return password

print(get_random_password())
