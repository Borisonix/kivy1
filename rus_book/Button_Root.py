# модуль Button_Root.py
from kivy.app import App
from kivy.lang import Builder

KV = """
BoxLayout:                  # контейнер (базовый класс BoxLayout)
    orientation: 'vertical'
    Button:                 # кнопка (класс Button)
        text: root.orientation     # свойство кнопки (надпись)
"""

class MainApp (App):
    def build (self):
        return Builder.load_string(KV)

MainApp().run()
