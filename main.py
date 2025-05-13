# main.py
import flet
from flet import Page
from model import Model
from view import View
from controller import Controller

def main(page: Page):
    model = Model()  # Создаем модель
    view = View(page)  # Создаем представление
    Controller(model, view)  # Создаем контроллер

flet.app(target=main)  
