# модуль RelativeLayout_11.py
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.relativelayout import RelativeLayout

KV = """
RelativeLayout:
    Button:
        size_hint:.2,.2
        pos_hint: {'x': 0, 'y': 0}
        text: 'B1'
    Button:
        size_hint:.2,.2
        pos_hint: {'right': 1, 'y': 0}
        text: 'B2'
    Button:
        size_hint:.2,.2
        pos_hint: {'center_x': .5, 'center_y':.5}
        text: 'B3'
    Button:
        size_hint:.2,.2
        pos_hint: {'x': 0, 'top': 1}
        text: 'B4'
    Button:
        size_hint:.2,.2
        pos_hint: {'right': 1, 'top': 1}
        text: 'B5'
"""

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run ()
