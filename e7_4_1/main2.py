from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MainApplication(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        btn1 = Button(text='Hello', size=(100, 50), size_hint=(None, None))
        btn2 = Button(text='Kivy', size_hint=(.5, 1))
        btn3 = Button(text='World', size_hint=(.5, 1))
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        return layout

if __name__=='__main__':
    MainApplication().run()

