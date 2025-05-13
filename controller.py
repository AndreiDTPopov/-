# controller.py
class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.slider.on_change = self.update_length
        
        self.view.btn_gen.on_click = self.generate_password
       
        self.view.btn_add.on_click = self.add_password

    def update_length(self, e):
        length = int(self.view.slider.value)
        self.view.len_text.value = f"Длина пароля: {length}"
        self.view.len_text.update()

    def generate_password(self, e):
        length = int(self.view.slider.value)
        password = self.model.gen_pass(length)
        self.view.result.value = f"Ваш пароль: {password}"
        self.view.result.update()

    def add_password(self, e):
        password = self.view.result.value.replace("Ваш пароль: ", "")
        if password:
            self.model.add_pass(password)
            self.view.pass_list.controls.append(Text(password))
            self.view.pass_list.update()
