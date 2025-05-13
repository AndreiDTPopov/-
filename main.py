# main.py
import flet
from flet import Page
from model import Model
from view import View
from controller import Controller
def main(page: Page):
    model = Model()  
    view = View(page)  
    Controller(model, view)  
    
flet.app(target=main)
