# модуль K_Image_1.py
from kivy.app import App
from kivy.uix.image import Image
class MainApp(App):
    def build (self):
        img = Image(source='./Images/img28.jpg')
        return img
MainApp().run()