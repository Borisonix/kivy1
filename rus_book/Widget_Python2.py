# модуль Widget_Python.py
from kivy.lang import Builder
from kivymd.app import MDApp
from  kivymd.uix.boxlayout import MDBoxLayout
from  kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainApp(MDApp):
    def build(self):
        BL = MDBoxLayout()
        but = Button(text='КНОПКА')
        but.bind(on_press=self.status)
        #but.bind(on_release=self.status)
        txt = TextInput()
        BL.add_widget(but)
        BL.add_widget(txt)
        return BL

    def status(self):
        print('Состояние кнопки – ' )

MainApp().run()