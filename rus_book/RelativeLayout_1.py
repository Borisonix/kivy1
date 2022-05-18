# модуль RelativeLayout_1.py
from kivy.app import App
from kivy.uix. button import Button
from kivy.uix.relativelayout import RelativeLayout

class MainApp(App):
    def build(self):
        rl = RelativeLayout()
        b1 = Button(size_hint=(.2,.2), pos_hint= {'x': 0, 'y': 0}, text='B1')
        b2 = Button(size_hint=(.2,.2), pos_hint= {'right': 1, 'y': 0}, text='B2')
        b3 = Button(size_hint=(.2,.2), pos_hint={'center_x': .5, 'center_y':.5}, text='B3')
        b4 = Button(size_hint=(.2,.2), pos_hint= {'x': 0, 'top': 1}, text='B4')
        b5 = Button(size_hint=(.2,.2), pos_hint= {'right': 1, 'top': 1}, text='B5')
        rl.add_widget(b1)
        rl.add_widget(b2)
        rl.add_widget(b3)
        rl.add_widget(b4)
        rl.add_widget(b5)
        return rl

MainApp().run ()
