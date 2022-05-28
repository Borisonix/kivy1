# модуль ScreenManager2.py
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

KV = '''
sm:
    Main_Screen:
    Screen_2:
    Screen_3:
<Main_Screen>:
    name: 'main'
    MDBoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Управление экранами'
        MDLabel:
            text: 'Это главный экран'
            halign: 'center'
        MDRaisedButton:
            text: 'К экрану 2 ->'
            pos_hint: {'center_x':.5, 'center_y':.5}
            on_release:
                app.root.current = 'second'
                root.manager.transition.direction = 'left'
# второй экран приложения
<Screen_2>:
    name: 'second'
    MDBoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Управление экранами'
        MDLabel:
            text: 'Это второй экран'
            halign: 'center'
        MDBoxLayout:
            orientation: 'horizontal'
            MDRaisedButton:
                text: '<-Назад'
                pos_hint: {'center_x':.5, 'center_y':.07}
                on_release:
                    app.root.current = 'main'
                    root.manager.transition.direction = 'right'
            MDLabel:
                text:''
            MDRaisedButton:
                text: 'К экрану 3 ->'
                pos_hint: {'center_x':.5,'center_y':.07}
                on_release:
                    app.root.current = 'third'
                    root.manager.transition.direction = 'left'
# третий экран приложения
<Screen_3>:
    name: 'third'
    MDBoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Управление экранами'
        MDLabel:
            text: 'Это третий экран'
            halign: 'center'
        MDRaisedButton:
            text: '<-Назад'
            on_release:
                app.root.current = 'second'
                root.manager.transition. direction = 'right'
'''


class Main_Screen(Screen):
    pass

class Screen_2(Screen):
    pass

class Screen_3(Screen):
    pass

class sm(ScreenManager):
    pass

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)


MainApp().run()
