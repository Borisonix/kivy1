# модуль Button_App.py
from kivy.app import App
from kivy.lang import Builder

KV = """
BoxLayout:                  # контейнер (базовый класс BoxLayout)
    orientation: 'vertical'
    Button:                 # кнопка (класс Button)
        text: 'Кнопка 1'     # свойство кнопки (надпись)
        on_press: app.press_button(self.text)
    Label:
        text: app.name
"""

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

    def press_button(self, instance):
        print('Вы нажали кнопку!')
        print(instance)

MainApp().run()
