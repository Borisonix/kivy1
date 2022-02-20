
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.event import EventDispatcher
from kivy.properties import *

class MyApp(App):
    def build(self):
        self.title = 'Моё приложение'
        return Label(text="Привет!!!")

if __name__ == '__main__':
    MyApp().run()
