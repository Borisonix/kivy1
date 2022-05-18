# модуль First_App_Kivy_MD2.py
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class MainApp(MDApp):
    def build(self):
        self.icon = 'icon.png'
        self.title = 'Приложение на KivyMD'
        label = MDLabel(text='Привет от KivyMD и Python!', halign='center')
        return label

if __name__ == '__main__':
    app = MainApp()       # Задание имени приложения
    app.run()            # запуск приложения

