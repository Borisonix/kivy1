# модуль AnchorLayout.py
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = AnchorLayout(anchor_x='right',
                              anchor_y='bottom',
                              padding=[40])
        btn1 = Button(text='Кнопка1', size_hint=(.3,.2))
        layout.add_widget(btn1)
        return layout


MyApp().run ()