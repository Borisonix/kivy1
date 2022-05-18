# модуль Scatter_22.py
from kivy.app import App
from kivy.lang import Builder

KV = """
<Picture@Scatter>:
    source: None
    size: image.size
    size_hint: None, None
    
    Image:
        id: image
        source: root.source

FloatLayout:
    Picture:
        source: './Images/1.jpg'
    Picture:
        source: './Images/2.jpg'
    Picture:
        source: './Images/3.jpg'
"""

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()
