# модуль Carousel_2.py
from kivy.app import App
from kivy.lang import Builder

KV = """
Carousel:
    direction: 'right'
    canvas:
        #Color:
        #   rgba: 0, 1, 0, 1
        Rectangle:
            source: './Images/img28.jpg'
            pos: self.pos
            size: self.size
    BoxLayout:
        Image:
            source: './Images/1.jpg'
    BoxLayout:
        Image:
            source: './Images/2.jpg'
    BoxLayout:
        Image:
            source: './Images/3.jpg'
"""

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()
