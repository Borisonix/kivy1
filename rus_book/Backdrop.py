# Модуль Backdrop.py
from kivymd.app import MDApp
from kivy.lang import Builder

KV = '''
MDScreen:
    MDBackdrop:                             # общие параметры backdrop
        id: backdrop
        header: True
        title: 'Заголовок заднего слоя'
        header_text: 'Заголовок переднего слоя'
        right_action_items: [['login', lambda x: print('Кнопка Вход')], ['apple', lambda x: print('Кнопка Apple')]]
        #padding: [20]              # Отступ подзаголовка от верхнего края
        #radius_right: '0dp'
        #radius_left: '0dp'
        close_icon: 'account'
        # параметры элементов заднего слоя
        MDBackdropBackLayer:
            MDFlatButton:
                text: 'Кнопка заднего слоя'
                pos_hint: {'center_x':0,'center_y':.5}
                on_press: app.callback1()
        # параметры элементов переднего слоя
        MDBackdropFrontLayer:
            MDFlatButton:
                text: 'Кнопка переднего слоя'
                pos_hint: {'center_x':.5,'center_y':.5}
                on_press: app.callback2()
'''
class Myapp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def callback1(self):
        # self.root.ids.backdrop.close()
        print('Нажата кнопка на заднем слое')

    def callback2(self):
        print('Нажата кнопка на переднем слое')

Myapp().run()