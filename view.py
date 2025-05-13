# view.py
import flet
from flet import Column, Slider, ElevatedButton, Text, ListView

class View:
    def __init__(self, page):
        self.page = page

        # Слайдер для выбора длины пароля
        self.slider = Slider(min=4, max=15, value=8, divisions=11, label="{value}")
        # Текст для отображения длины
        self.len_text = Text(value=f"Длина пароля: {int(self.slider.value)}", size=16)
        # Кнопка для генерации пароля
        self.btn_gen = ElevatedButton(text="Сгенерировать")
        # Кнопка для добавления пароля в список
        self.btn_add = ElevatedButton(text="Добавить в список")
        # Текст для вывода результата
        self.result = Text(value="", size=20)
        # Список для хранения паролей
        self.pass_list = ListView()

        # Компоновка элементов
        self.page.title = "Генератор паролей"
        self.page.add(
            Column(
                controls=[
                    self.len_text,
                    self.slider,
                    self.btn_gen,
                    self.result,
                    self.btn_add,
                    self.pass_list
                ],
                spacing=10,
                horizontal_alignment="center",
                width=300
            )
        )
