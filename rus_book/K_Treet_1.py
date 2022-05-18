# модуль K_Tree_1.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix. button import Button
from kivy.uix.screenmanager import Screen


class MainApp(App):
    def build (self):
        scr = Screen() # корневой виджет (экран)
        box = BoxLayout() # контейнер box
        but1 = Button(text='Кнопка 1')      # кнопка 1
        but2 = Button (text='Кнопка 2')     # кнопка 2
        box.add_widget(but1)    # положить кнопку 1 в контейнер
        box.add_widget(but2)    # положить кнопку 2 в контейнер
        scr.add_widget(box)     # положить контейнер в корневой виджет
        return scr


MainApp().run ()