# модуль Widget_Python.py
from kivy.lang import Builder
from kivymd.app import MDApp

KV = """
MDBoxLayout:
    Button:
        id: but
        text: 'КНОПКА'
        on_press: app.status(txt.text)
        on_release: app.status(txt.text)
    TextInput:
        id: txt
        text: but.state
"""

class MainApp (MDApp):
    def build(self):
        return Builder.load_string(KV)

    def status(self, stt):
        print('Состояние кнопки – ' + stt)

MainApp().run ()