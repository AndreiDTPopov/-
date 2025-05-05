import string
import random
class PasswordModel:
    def __init__(self):
        self.length = 12
        self.min_length = 6
        self.max_length = 20
        self.use_uppercase = True
        self.use_lowercase = True
        self.use_digits = True
        self.use_symbols = True
    def generate_password(self) -> str:
        chars = ""
        if self.use_uppercase:
            chars += string.ascii_uppercase
        if self.use_lowercase:
            chars += string.ascii_lowercase
        if self.use_digits:
            chars += string.digits
        if self.use_symbols:
            chars += string.punctuation
        if not chars:
            return "Ошибка: выберите хотя бы один тип символов!"
        length = max(self.min_length, min(self.length, self.max_length))
        return ''.join(random.choice(chars) for _ in range(length))
