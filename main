import flet
from model import PasswordModel
from view import PasswordView
from controller import PasswordController
def main(page: flet.Page):
    model = PasswordModel()
    view = PasswordView(page)
    controller = PasswordController(model, view)
if __name__ == "__main__":
    flet.app(target=main, view=flet.WEB_BROWSER)
