# модуль ScreenManager.py
from kivy.app import App
from kivy.lang import Builder
from kivy.graphics.svg import Window
from kivy.uix.screenmanager import ScreenManager, Screen

KV = """
# менеджер экранов
WindowManager:
    MainWindow:
    Screen_2:
    Screen_3:
# главный экран приложения
<MainWindow>:
    name: 'main'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Главный экран'
        Button:
            text: 'К экрану 2 ->'
            size_hint: (.2,.1)
            on_release:
                app.root.current = 'second'
                root.manager.transition.direction = 'left'
# второй экран приложения
<Screen_2>:
    name: 'second'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Это второй экран'
        Button:
            text: '<-Назад'
            size_hint: (.2,.1)
            on_release:
                app.root.current = 'main'
                root.manager.transition.direction = 'right'
        Button:
            text: 'К экрану 3 ->'
            size_hint: (.2,.1)
            on_release:
                app.root.current = 'third'
                root.manager.transition.direction = 'left'
# третий экран приложения
<Screen_3>:
    name: 'third'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Это третий экран'
        Button:
            text: "<-Назад"
            size_hint: (.2,.1)
            on_release:
                app.root.current = 'second'
                root.manager.transition.direction = 'right'
"""
# главный экран приложения
class MainWindow(Screen):
    pass

# второй экран приложения
class Screen_2(Screen):
    pass

# третий экран приложения
class Screen_3(Screen):
    pass

# менеджер экранов
class WindowManager(ScreenManager):
    pass

kv = Builder.load_string(KV)

Window.size = (360, 600)

class MyMainApp(App):
    def build(self):
        return kv

MyMainApp().run ()