# K_ProgressBar_2
from kivy.app import App
from kivy.lang import Builder

KV = """
ProgressBar:
    max: 1000
    value: 650
"""


class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()