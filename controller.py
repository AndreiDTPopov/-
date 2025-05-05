from flet import SnackBar, Text
class PasswordController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        view.generate_btn.on_click = self.generate_password
        view.copy_btn.on_click = self.copy_password
        view.length_input.on_change = self.update_length
        view.uppercase_cb.on_change = self.update_uppercase
        view.lowercase_cb.on_change = self.update_lowercase
        view.digits_cb.on_change = self.update_digits
        view.symbols_cb.on_change = self.update_symbols
    def update_length(self, e):
        try:
            length = int(self.view.length_input.value)
            length = max(self.model.min_length, min(length, self.model.max_length))
            self.model.length = length
            if str(length) != self.view.length_input.value:
                self.view.length_input.value = str(length)
                self.view.length_input.update()
        except ValueError:
            self.view.length_input.value = str(self.model.length)
            self.view.length_input.update()
def update_uppercase(self, e):
        self.model.use_uppercase = self.view.uppercase_cb.value
    def update_lowercase(self, e):
        self.model.use_lowercase = self.view.lowercase_cb.value
    def update_digits(self, e):
        self.model.use_digits = self.view.digits_cb.value
    def update_symbols(self, e):
        self.model.use_symbols = self.view.symbols_cb.value
    def generate_password(self, e):
        password = self.model.generate_password()
        self.view.password_output.value = password
        self.view.password_output.update()
    def copy_password(self, e):
        pw = self.view.password_output.value
        if pw and not pw.startswith("Ошибка"):
            self.view.page.set_clipboard(pw)
            self.view.snackbar = SnackBar(Text("Пароль скопирован!"))
            self.view.snackbar.open = True
            self.view.page.update()
