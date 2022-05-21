# модуль platej_kivy2.py
from kivy.app import App

class Platej(App):

    def raschet(self, tinp_summa, tinp_proc, tinp_k_mes):
        s = int(tinp_summa)
        p = float(tinp_proc)
        n = int(tinp_k_mes)
        i = p / 12 / 100
        a = s * i / (1 - (1 / (1 + i)) ** n)
        a = round(a, 2)
        return str(a)

MainApp = Platej()
MainApp.title = "Расчет ежемесячного аннуитентного платежа"

MainApp.run()