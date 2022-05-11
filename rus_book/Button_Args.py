# модуль Button_Args.py
from kivy.app import App
from kivy.lang import Builder

KV = """
BoxLayout:                  # контейнер (базовый класс BoxLayout)
    orientation: 'vertical'
    Button:                 # кнопка (класс Button)
        text: 'Кнопка 1'     # свойство кнопки (надпись)
        on_press: app.press_button(*args)
    TextInput:
        on_focus: self.insert_text('Фокус' if args[1] else 'Нет')
"""

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

    def press_button(self, instance):
        print('Вы нажали кнопку!')
        print(instance)

MainApp().run()
