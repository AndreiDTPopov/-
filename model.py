# model.py
import random
import string
class Model:
    def __init__(self):
        self.passwords = []  # Список для хранения паролей
    def gen_pass(self, length):
        # Генерация пароля из букв, цифр и символов
        chars = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(chars) for _ in range(length))
    def add_pass(self, password):
        # Добавление пароля в список
        self.passwords.append(password)
