# модуль First_App_Kivy2.py
from kivy.app import App
from kivy.uix.label import Label

class MainApp(App):    # формирование базового класса приложения
    def build(self):            # формирование функции в базовом классе
        self.title = 'Приложение на Kivy'
        self.icon = 'icon.png'
        label = Label(text='Привет от Kivy и Python!')
        return label

if __name__ == '__main__':
    app = MainApp()       # Задание имени приложения
    app.run()            # запуск приложения