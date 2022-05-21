# модуль GridLayout_2.py
from kivy.app import App
from kivy.lang import Builder

KV = """
GridLayout:
    cols: 2
    rows: 5
    row_force_default: True     # будет проигнорирована высота (size_hint_y) дочернего элемента
    row_default_height: 50
    Label:
        text: 'Сумма остатка кредита, руб:'
    TextInput:
        id: tinp_summa
        text: '2455000'
        size_hint:.5,.3
    Label:
        text: 'Процентная ставка, %:'
    TextInput:
        id: tinp_proc
        text: '9'
        size_hint:.5,.3
    Label:
        text: 'Кол-во месяцев: '
    TextInput:
        id: tinp_k_mes
        text: '240'
        size_hint:.5,.3
    Label:
        text: 'Размер аннуитентного платежа, руб: '
        font_size: 24
        halign: 'left'
    Label:
        text: ''
        align: 'left'
        id: lbl_plata
        size_hint:.5,.3
        font_size: 24
    Button:
        text: 'Расчитать'
        on_press: lbl_plata.text = app.raschet(tinp_summa.text, tinp_proc.text, tinp_k_mes.text)
"""


class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

    def raschet(self, tinp_summa, tinp_proc, tinp_k_mes):
        s = int(tinp_summa)
        p = float(tinp_proc)
        n = int(tinp_k_mes)
        i = p / 12 / 100
        a = s * i / (1 - (1 / (1 + i)) ** n)
        a = round(a, 2)
        # print(f'Размер аннуитентного платежа: {a} руб в месяц')
        return str(a)


MainApp().run()