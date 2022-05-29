# модуль Bottom_Navi.py
from kivymd.app import MDApp
from kivy.lang import Builder
KV = """
MDBoxLayout:
    orientation: 'vertical'
    MDToolbar:
        title: 'Пример Bottom Navigation'
        
        MDBottomNavigation:
            panel_color: 255/255, 255/255, 204/255, 1
            #panel_color: 0, 0, 1, 1
            MDBottomNavigationItem:
                name: 'screen 1'
                text: 'Python'
                icon: 'language-python'
                MDLabel:
                    text: 'Вкладка программирование на Python'
                    halign: 'center'
            MDBottomNavigationItem:
                name: 'screen 2'
                text: 'C++'
                icon: 'language-cpp'
                MDLabel:
                    text: 'Вкладка программирование на C++'
                    halign: 'center'
            MDBottomNavigationItem:
                name: 'screen 3'
                text: 'Java'
                icon: 'language-javascript'
                MDLabel:
                    text: 'Вкладка программирование на Java Script'
                    halign: 'center'
"""

class Myapp(MDApp):
    def build(self):
        return Builder.load_string(KV)

Myapp().run()