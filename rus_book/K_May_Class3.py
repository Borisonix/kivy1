# модуль K_May_Class3.py
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

KV = """
<MyBox@BoxLayout>
MyBox:                      # контейнер (пользовательский  класс)
    Button:                 # кнопка (класс Button)
        text: "Кнопка 3"    # свойство кнопки (надпись)
"""

class MainApp (App):
    def build (self):
        return Builder.load_string(KV)

MainApp().run()
