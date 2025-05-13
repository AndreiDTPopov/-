# model.py
import random
import string

class Model:
    def __init__(self):
        self.passwords = []  

    def gen_pass(self, length):
        
        chars = string.ascii_letters + string.digits + string.punctuation + " " 
        return ''.join(random.choice(chars) for _ in range(length))

    def add_pass(self, password):
        
        self.passwords.append(password)
