# модуль GridLayout_2.py
from kivy.app import App
from kivy.lang import Builder

KV = """
GridLayout:
    cols: 2
    rows: 2
    row_force_default: True     # будет проигнорирована высота (size_hint_y) дочернего элемента
    row_default_height: 40
    Button:
        text: 'Кнопка 1'
        size_hint_x: None
    Button:
        text: 'Кнопка 2'
        size_hint:.5,.3
    Button:
        text: 'Кнопка 3'
        size_hint_x: None
    Button:
        text: 'Кнопка 4'
        size_hint:.5,.3
"""


class MainApp(App):
    def build(self):
        return Builder.load_string(KV)


MainApp().run()