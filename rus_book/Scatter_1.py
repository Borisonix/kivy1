# модуль Scatter_1.py
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.scatter import Scatter

class MainApp(App):
    def build(self):
        rl = RelativeLayout()
        sct = Scatter()
        img = Image(source='111.jpg')
        sct.add_widget(img)
        rl.add_widget(sct)
        return rl


MainApp().run ()