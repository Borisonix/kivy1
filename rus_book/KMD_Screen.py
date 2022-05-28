# модуль KMD_Screen.py
from kivymd. app import MDApp
from kivymd.uix.label import MDLabel
from kivymd. uix.button import MDRectangleFlatButton
from kivy.uix.screenmanager import Screen


class MainApp(MDApp):
    def build(self):
        screen = Screen()
        screen.add_widget(MDLabel(text='Привет от KivyMD!', halign='center'))
        screen.add_widget(MDRectangleFlatButton(text='Кнопка KMD', pos_hint= {'center_x': 0.5, 'center_y': 0.4}))
        return screen

MainApp().run()
