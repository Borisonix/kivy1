# модуль K_Tree_2.py
from kivy.app import App
from kivy.lang import Builder

KV = """
Screen:                         # создание корневого виджета (экран)
    BoxLayout:                  # создание контейнера BoxLayout
        Button:                 # добавление в контейнер виджета Button (кнопка)
            text: 'Кнопка 1'
        Button:                 # добавление в контейнер виджета Button (кнопка)
            text: 'Кнопка 2'
"""


class MainApp(App):
    def build(self):
        return Builder.load_string(KV)


MainApp().run()