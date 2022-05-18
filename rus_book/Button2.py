# Button2.py
from kivy.app import App
from kivy.lang import Builder

KV = """
Button:
    text: 'Кнопка2'
    size_hint: None, None
    size: 150, 50
    pos: 100, 50
"""


class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()