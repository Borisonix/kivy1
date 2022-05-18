# Button_Color.py
from kivy.app import App
from kivy.lang import Builder

KV = """
GridLayout:
    cols: 3
    rows: 2
    Button:
        text: 'Красный'
        background_color: 1, 0, 0, 1
    Button:
        text: 'Зеленый'
        background_color: 0, 1, 0, 1
    Button:
        text: 'Синий'
        background_color: 0, 0, 1, 1
    Button:
        text: 'Черный'
        background_color: 0, 0, 0, 1
    Button:
        text: 'Белый'
        color: 0,0,0,1
        background_normal: ''
    Button:
        text: 'Бирюзовый'
        background_color: 102/255, 255/255, 255/255, 1
"""


class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()