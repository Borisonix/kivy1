import kivy.app
import kivy.uix.label

class MainApp(kivy.app.App):    # формирование базового класса приложения
    def build(self):            # формирование функции в базовом классе
        return kivy.uix.label.Label(text='Привет от Kivy!')

app = MainApp(title='Первое приложение на Kivy')       # Задание имени приложения

app.run ()                                              # запуск приложения