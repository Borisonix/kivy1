# модуль Scatter_22.py
from kivy.app import App
from kivy.lang import Builder

KV = """
<MyBut@Button>
    font_size: 15
    size_hint:.2,.1
StackLayout:
    orientation: 'rl-tb'
    padding: [5, 10]
    spacing: 10
    MyBut:
        text: 'B1'
    MyBut:
        text: 'B2'
    MyBut:
        text: 'B3'
    MyBut:
        text: 'B4'
    MyBut:
        text: 'B5'
    MyBut:
        text: 'B6'
    MyBut:
        text: 'B7'
    MyBut:
        text: 'B8'
    MyBut:
        text: 'B9'
    MyBut:
        text: 'B10'
"""

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()
