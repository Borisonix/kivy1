# модуль AnchorLayout_2.py
from kivy.app import App
from kivy.lang import Builder

KV = """
BoxLayout:
    orientation: 'vertical'
    padding: [50, 50, 50, 50]
    spacing: 10
    Button:
        text: 'Кнопка 1'
    Button:
        text: 'Кнопка 2'
    Button:
        text: 'Кнопка 3'
    Button:
        text: 'Кнопка 4'
"""


class MainApp(App):
    def build(self):
        return Builder.load_string(KV)


MainApp().run()