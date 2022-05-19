# модуль Scatter_22.py
from kivy.app import App
from kivy.lang import Builder

KV = """
RelativeLayout:
    canvas:
        Rectangle:
            source: '16_format.png'
            size: self.size
            pos: self.pos
    ScatterLayout:
        Image:
            source: '111.jpg'
"""

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()
