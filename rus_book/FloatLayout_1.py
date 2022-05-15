# модуль FloatLayout_1.py
from kivy.app import App
from kivy.lang import Builder

KV = """
FloatLayout:
    Button:
        text: 'Кнопка'
        size_hint: .3,.2
        pos: 30, 30
"""


class MainApp(App):
    def build(self):
        return Builder.load_string(KV)


MainApp().run()