# view.py
import flet
from flet import Column, Slider, ElevatedButton, Text, ListView

class View:
    def __init__(self, page):
        self.page = page

       
        self.slider = Slider(min=4, max=15, value=8, divisions=11, label="{value}")
      
        self.len_text = Text(value=f"Длина пароля: {int(self.slider.value)}", size=16)
   
        self.btn_gen = ElevatedButton(text="Сгенерировать")
       
        self.btn_add = ElevatedButton(text="Добавить в список")
        
        self.result = Text(value="", size=20)
       
        self.pass_list = ListView()

      
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
