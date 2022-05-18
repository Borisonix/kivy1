# K_Video_2.py
from kivy.app import App
from kivy.lang import Builder

KV = """
Video:
    source: 'ug.mp4'
    state: 'play'
"""

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()