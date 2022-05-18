# модуль Button_Self.py
from kivy.app import App
from kivy.lang import Builder

KV = """
Button
    text: f'Состояние кнопки - {self.state}'
"""

class MainApp (App):
    def build (self):
        return Builder.load_string(KV)

MainApp().run()
