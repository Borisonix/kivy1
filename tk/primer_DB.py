

from tkinter import *
import tkinter as tk
from tkinter import ttk

import datetime
import xlsxwriter
import pymysql
from xlsxwriter.workbook import Workbook
from tkinter import messagebox
import sys

##DB##
try:
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='Kep_if', charset='utf8')
except Exception as e:
    messagebox.showerror("Помилка!", "Відсутнє з'єднання з базою даних.Підключітся до бази даних!")
    sys.exit("Error!")


###############1#####################


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

    def open_dialog(self):
        Child()

    def open_dialog1(self):
        Child1()

    def open_dialog2(self):
        Child2()


class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()

    def init_child(self):
        self.title('Помічник секретаря')
        self.geometry('950x700')
        self.config(bg='light blue')

        self.label_com = Label(self, text="Виберіть дію", font=25, bg='light blue')
        self.label_com.place(x=350, y=10)
        self.but_add_grup = Button(self, text="Добавити студента", font=15, height=5, width=25, command=Child1,
                                   bg='light grey')
        self.but_add_grup.place(x=280, y=50)
        self.but_add_grup.bind("<Button-1>")

        self.but_add_grup = Button(self, text="Добавити групу", font=15, height=5, width=25, bg='light grey',
                                   command=Child2)
        self.but_add_grup.place(x=280, y=180)
        self.but_add_grup.bind("<Button-1>")

        self.but_add_vuk = Button(self, text="Добавити викладача", font=15, height=5, width=25, bg='light grey',
                                  command=Child4)
        self.but_add_vuk.place(x=280, y=310)
        self.but_add_vuk.bind("<Button-1>")

        self.but_add_vuk = Button(self, text="Добавити придмет", font=15, height=5, width=25, bg='light grey',
                                  command=Child5)
        self.but_add_vuk.place(x=280, y=440)
        self.but_add_vuk.bind("<Button-1>")

        self.but_add_ocinka = Button(self, text="Добавити оцінки", font=15, height=5, width=25, bg='light grey',
                                     command=Child6)
        self.but_add_ocinka.place(x=280, y=570)
        self.but_add_ocinka.bind("<Button-1>")
        self.focus_set()
        self.grab_release()


###############2#####################s##########################################
################################################################################
# Studenta!
################################################################################


class Child1(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child1()

    def init_child1(self):
        self.title('Помічник секретаря')
        self.geometry('1000x500')
        self.config(bg='light blue')
        self.text1 = Label(self, text="Номер залікової книжки", font=15, bg='light blue')
        self.text2 = Label(self, text="Прізвище", font=15, bg='light blue')
        self.text3 = Label(self, text="Імя", font=15, bg='light blue')
        self.text4 = Label(self, text="Побатькові", font=15, bg='light blue')
        self.text5 = Label(self, text="Група", font=15, bg='light blue')
        self.text6 = Label(self, text="форма оплати", font=15, bg='light blue')
        self.text7 = Label(self, text="Виберіть куратора", font=15, bg='light blue')

        self.text1.grid(row=0, column=0)
        self.text2.grid(row=0, column=1)
        self.text3.grid(row=0, column=2)
        self.text4.grid(row=0, column=3)
        self.text5.grid(row=0, column=4)
        self.text6.grid(row=0, column=5)
        self.text7.grid(row=0, column=6)

        self.b1 = Entry(self)
        self.b1.grid(row=1, column=0)
        self.b2 = Entry(self)
        self.b2.grid(row=1, column=1)
        self.b3 = Entry(self)
        self.b3.grid(row=1, column=2)
        self.b4 = Entry(self)
        self.b4.grid(row=1, column=3)
        self.b5 = Entry(self)
        self.b5.grid(row=1, column=4)
        self.b6 = Entry(self)
        self.b6.grid(row=1, column=5)

        self.button_add = Button(self, text="Добавити", font=15, command=self.add1)
        self.button_add.place(x=400, y=100)
        self.button_add.bind("<Button-1>", )

        n2 = ("Select ПІБ from Викладачі")
        cur = conn.cursor()
        cur.execute(n2)
        self.s2 = cur.fetchall()
        cur.close()

        self.k = tk.StringVar()
        self.combo = ttk.Combobox(self, height=3, foreground='#FF0000', state="readonly", textvariable=self.k)
        self.combo['values'] = list(self.s2)
        self.combo.grid(row=1, column=6)

        self.resizable(False, False)
        self.overrideredirect(False)
        self.grab_set()
        self.focus_set()

    def add1(self):
        a1 = (self.b1.get())
        a2 = (self.b2.get())
        a3 = (self.b3.get())
        a4 = (self.b4.get())
        a5 = (self.b5.get())
        a6 = (self.b6.get())

        idd = self.combo.current()
        print(idd)
        if ((len(a1) != 0) and (len(a2) != 0) and (len(a3) != 0) and (len(a4) != 0) and (len(a5) != 0) and (
                len(a6) != 0)):
            cur1 = conn.cursor()
            dbmys = (
                """INSERT INTO Студенти(Номер_залікової_книжки, Прізвище, Імя, Побатькові, Група, Форма_навчання,  Куратор) values (%s,%s,%s,%s,%s,%s,%s)""")
            z = (a1, a2, a3, a4, a5, a6, idd)
            cur1.execute(dbmys, z)
            cur1.close()

            self.b1.delete(0, 'end')
            self.b2.delete(0, 'end')
            self.b3.delete(0, 'end')
            self.b4.delete(0, 'end')
            self.b5.delete(0, 'end')
            self.b6.delete(0, 'end')
            self.combo.select_range(0, END)
        else:
            messagebox.showerror("Увага!", "Перевірте чи правельно введенні дані!")

        conn.commit()


###################################################################################
###################################################################################
# GRUPU !
###################################################################################
class Child2(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child2()

    def init_child2(self):
        self.title('Помічник секретаря')
        self.geometry('900x500')
        self.config(bg='light blue')

        self.name_grup = Label(self, text="Введіть назву групи", font=15, bg='light blue')
        self.name_grup.place(x=1, y=1)

        self.name_kyrator = Label(self, text="Виберіть куратора", font=15, bg='light blue')
        self.name_kyrator.place(x=190, y=1)

        self.e_name_grup = Entry(self)
        self.e_name_grup.place(x=5, y=20)

        n = ("Select ПІБ from Викладачі")
        cur = conn.cursor()
        cur.execute(n)
        self.s1 = cur.fetchall()

        self.v1 = tk.StringVar(self)
        self.combo_box_kur = ttk.Combobox(self, height=5, width=30, foreground='#FF0000', state='readonly',
                                          textvariable=self.v1)
        self.combo_box_kur['values'] = list(self.s1)
        self.combo_box_kur.place(x=200, y=20)
        ##Випадаючий список викладачів
        # self.user = tk.StringVar()
        # self.kyrator12 = ttk.Combobox(self, height=3, foreground='#FF0000', state='readonly', textvariable=self.user)
        # self.kyrator12['values'] = list(self.s1)
        # self.kyrator12.place(x=200, y=20)
        self.combo_box_kur.bind('<<ComboboxSelected>>', self.perevirka)

        ###################################
        self.button_add_grup1 = Button(self, text="Добавити", command=Child3, font=15, )
        self.button_add_grup1.place(x=400, y=100)
        self.button_add_grup1.bind("<Button-1>", )
        cur.close()
        self.resizable(False, False)
        self.overrideredirect(False)

    def perevirka(self, e):
        global NameG
        global id_kur
        NameG = (self.e_name_grup.get())
        print(NameG)
        kyr_combo = self.v1.get()  # НАЗВА ВИКЛАДАЧА
        print(kyr_combo)
        id_kur = self.combo_box_kur.current()  # ІД ВИКЛАДАЧА
        print(id_kur)


###################################################################################
###################################################################################
# GRUPU
###################################################################################


class Child3(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child3()

    def init_child3(self):
        self.title('Помічник секретаря')
        self.geometry('900x500')
        self.config(bg='light blue')

        self.text1 = Label(self, text="Номер залікової книжки", font=15, bg='light blue')
        self.text2 = Label(self, text="Прізвище", font=15, bg='light blue')
        self.text3 = Label(self, text="Імя", font=15, bg='light blue')
        self.text4 = Label(self, text="Побатькові", font=15, bg='light blue')
        self.text5 = Label(self, text="Форма оплати", font=15, bg='light blue')

        self.text1.grid(row=0, column=0)
        self.text2.grid(row=0, column=1)
        self.text3.grid(row=0, column=2)
        self.text4.grid(row=0, column=3)
        self.text5.grid(row=0, column=4)
        self.b1 = Entry(self)
        self.b1.grid(row=1, column=0)
        self.b2 = Entry(self)
        self.b2.grid(row=1, column=1)
        self.b3 = Entry(self)
        self.b3.grid(row=1, column=2)
        self.b4 = Entry(self)
        self.b4.grid(row=1, column=3)
        self.b5 = Entry(self)
        self.b5.grid(row=1, column=4)

        self.button_add = Button(self, text="Добавити", font=15, command=self.add12)
        self.button_add.place(x=400, y=100)
        self.button_add.bind("<Button-1>", )

        self.resizable(False, False)
        self.overrideredirect(False)
        self.grab_set()
        self.focus_set()

    def add12(self):
        a1 = (self.b1.get())
        a2 = (self.b2.get())
        a3 = (self.b3.get())
        a4 = (self.b4.get())
        a5 = (self.b5.get())
        if ((len(a1) != 0) and (len(a2) != 0) and (len(a3) != 0) and (len(a4) != 0) and (len(a5) != 0)):
            cur1 = conn.cursor()
            dbmys2 = ("""INSERT INTO Студенти(Номер_залікової_книжки, Прізвище, Імя, Побатькові, Група, Форма_навчання, Куратор)
             values (%s,%s,%s,%s,%s,%s,%s)""")

            z1 = (a1, a2, a3, a4, str(NameG), a5, int(id_kur))  # комбо бокс викладачів
            cur1.execute(dbmys2, z1)
            cur1.close()
            conn.commit()
            self.b1.delete(0, 'end')
            self.b2.delete(0, 'end')
            self.b3.delete(0, 'end')
            self.b4.delete(0, 'end')
            self.b5.delete(0, 'end')
        else:
            messagebox.showerror("Увага!", "Перевірте чи правельно введенні дані!")


###################################################################################
###################################################################################
# VUKLADACHA!
###################################################################################
class Child4(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child4()

    def init_child4(self):

        self.title('Помічник секретаря')
        self.geometry('900x500')
        self.config(bg='light blue')

        self.name_vuk = Label(self, text="Введіть ПІБ Викладача", font=15, bg='light blue')
        self.name_vuk.grid(row=0, column=1)

        self.entri_name_vuk = Entry(self, width=40, )
        self.entri_name_vuk.grid(row=1, column=3, )

        self.button_add_vuk = Button(self, text="Добавити", font=15, command=self.add_vuk)
        self.button_add_vuk.grid(row=50, column=3)
        self.button_add_vuk.bind("<Button-1>", )

        self.resizable(False, False)
        self.overrideredirect(False)

    def add_vuk(self):
        pib_vuk = (self.entri_name_vuk.get())
        if (len(pib_vuk) != 0):
            cur2 = conn.cursor()
            db1 = (""" INSERT INTO Викладачі( ПІБ) values(%s)""")
            z1 = (pib_vuk)
            cur2.execute(db1, z1)
            cur2.close()

            conn.commit()
            self.entri_name_vuk.delete(0, 'end')
        else:
            messagebox.showerror("Увага!", "Перевірте чи правельно введенні дані!")


###################################################################################
###################################################################################
# PRUDMET!333
###################################################################################
class Child5(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child5()

    def init_child5(self):

        self.title('Помічник секретаря')
        self.geometry('1000x700')
        self.config(bg='light blue')
        self.name_sub = Label(self, text="Введіть назву придмету", font=15, bg='light blue')
        self.name_sub.place(x=1, y=0)

        self.entri_name_sub = Entry(self)
        self.entri_name_sub.place(x=20, y=20)

        self.label_vuk = Label(self, text="Виберіть викладача ", font=15, bg='light blue')
        self.label_vuk.place(x=190, y=0)

        self.label_g = Label(self, text="Виберіть групу", font=15, bg='light blue')
        self.label_g.place(x=390, y=0)

        self.label_s = Label(self, text="Виберіть семестр", font=15, bg='light blue')
        self.label_s.place(x=520, y=0)

        self.label_kg = Label(self, text="Введіть кількість годин", font=15, bg='light blue')
        self.label_kg.place(x=680, y=0)

        name_vuk = ("Select ПІБ from Викладачі")
        cur8 = conn.cursor()
        cur8.execute(name_vuk)
        self.s1 = cur8.fetchall()
        # combobox vukladachiv
        self.v = tk.StringVar()
        self.combo_box = ttk.Combobox(self, height=5, width=25, foreground='#FF0000', state='readonly',
                                      textvariable=self.v)
        self.combo_box['values'] = list(self.s1)
        self.combo_box.place(x=180, y=20)

        # combobox grupa
        curs = conn.cursor()

        self.box_grup1 = ("Select Група from Студенти group by Група;")
        curs.execute(self.box_grup1)
        self.e4 = curs.fetchall()

        self.v1 = tk.StringVar()
        self.combo_box1 = ttk.Combobox(self, height=5, width=20, foreground='#FF0000', state='readonly',
                                       textvariable=self.v1)
        self.combo_box1['values'] = list(self.e4)
        self.combo_box1.place(x=380, y=20)

        ######## combobox semestr

        self.v2 = tk.StringVar()
        self.combo_box2 = ttk.Combobox(self, height=5, width=20, foreground='#FF0000', state='readonly',
                                       textvariable=self.v2)
        self.combo_box2['values'] = ('1', '2', '3', '4', '5', '6', '7', '8')
        self.combo_box2.place(x=520, y=20)

        #####kilkist godun
        self.kg = Entry(self)
        self.kg.place(x=680, y=20)

        self.CheckVar1 = IntVar()
        self.ekz1 = Checkbutton(self, text="Це екзамен", font=15, bg='light blue', variable=self.CheckVar1, onvalue=1,
                                offvalue=0)
        self.ekz1.place(x=870, y=15)

        self.button_add_sub = Button(self, text="Добавити", font=20, command=self.add_subject)
        self.button_add_sub.place(x=400, y=100)
        self.button_add_sub.bind("<Button-1>", )

    def add_subject(self):
        name_sub1 = (self.entri_name_sub.get())
        print(name_sub1)

        gr = self.v1.get()
        print(gr)

        semestr = self.v2.get()
        print(semestr)

        id_vukladacha = self.combo_box.current()
        print(id_vukladacha)

        kol_god = (self.kg.get())
        print(kol_god)

        self.chk = self.CheckVar1.get()
        print(self.chk)

        if (len(name_sub1) != 0 and len(kol_god) != 0):
            cur2 = conn.cursor()
            db1 = (""" INSERT INTO Студенти_has_Предмети(Група,Предмет,Семестр,Кількість_год,Екзамен,Викладачі_idВикладачі)
             values(%s,%s,%s,%s,%s,%s)""")
            z1 = (gr, name_sub1, semestr, kol_god, self.chk, id_vukladacha)  #
            cur2.execute(db1, z1)
            cur2.close()
            self.entri_name_sub.delete(0, 'end')
            self.kg.delete(0, 'end')
            self.combo_box.select_range(0, END)
            self.combo_box1.select_range(0, END)
            self.combo_box2.select_range(0, END)
            conn.commit()
        else:
            messagebox.showerror("Увага!", "Перевірте чи правельно введенні дані!")


###########################################################################
# OCINKA???
###################################################################################

class Child6(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child6()

    def init_child6(self):
        self.title('Помічник секретаря')
        self.geometry('900x500')
        self.config(bg='light blue')
        self.vub_sub = Label(self, text="Виберіть придмет", font=15, bg='light blue')
        self.vub_sub.place(x=1, y=1)
        curs1 = conn.cursor()
        self.box_pred = ("Select Предмет from Студенти_has_Предмети")

        curs1.execute(self.box_pred)
        c = curs1.fetchall()

        self.pred = tk.StringVar()
        self.combo_box_sub = ttk.Combobox(self, height=3, foreground='#FF0000', state='readonly',
                                          textvariable=self.pred)
        self.combo_box_sub['values'] = c
        self.combo_box_sub.place(x=10, y=20)

        self.vub_grup = Label(self, text="Виберіть групу", font=15, bg='light blue')
        self.vub_grup.place(x=200, y=1)

        curs = conn.cursor()

        self.box_grup = ("Select Група from Студенти group by Група;")
        curs.execute(self.box_grup)
        self.e3 = curs.fetchall()

        self.grup = tk.StringVar()
        self.combo_box_grup = ttk.Combobox(self, height=3, foreground='#FF0000', state='readonly',
                                           textvariable=self.grup)
        self.combo_box_grup['values'] = list(self.e3)
        self.combo_box_grup.place(x=200, y=20)

        self.vub_mis = Label(self, text="Виберіть місяць", font=15, bg='light blue').place(x=380, y=2)

        self.mis = tk.StringVar()
        self.combo_box_mis = ttk.Combobox(self, height=3, foreground='#FF0000', state='readonly', textvariable=self.mis)
        self.combo_box_mis['values'] = (
        'Вересень', 'Жовтень', 'Листопад', 'Грудень', 'Січень', 'Лютий', 'Березень', 'Квітень', 'Травень', 'Червень',
        'Липень', 'Серпень')
        self.combo_box_mis.bind('<<ComboboxSelected>>', self.cur)
        self.combo_box_mis.place(x=380, y=20)

        self.button_pidtverdutu = Button(self, text="Підтвердити", font=20, command=Child7)
        self.button_pidtverdutu.place(x=400, y=100)
        self.button_pidtverdutu.bind("<Button-1>", )

        self.CheckVar2 = IntVar()
        self.ekz = Checkbutton(self, text="Це екзамен", font=15, bg='light blue', variable=self.CheckVar2, onvalue=1,
                               offvalue=0)
        self.ekz.place(x=530, y=15)

        self.resizable(False, False)
        self.overrideredirect(False)

    def cur(self, e):
        global data
        global pred
        global Ekzamen
        Ekzamen = self.CheckVar2.get()

        data = self.combo_box_mis.current()
        print(data)
        pred = self.combo_box_sub.current()
        print(pred)
        G_r = self.combo_box_grup.current()
        print(G_r)


class Child7(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child7()

    def init_child7(self):
        self.title('Помічник секретаря')
        self.geometry('900x500')
        self.config(bg='light blue')
        s = ("Select* from Студенти")
        cur3 = conn.cursor()
        cur3.execute(s)
        self.s1 = cur3.fetchall()

        ###############################################
        y = 10
        self.k = 0
        for a in self.s1:
            self.nam = a[1] + " " + a[2] + " " + a[3]
            print(self.nam)

            self.text = Label(self, text=self.nam, font=15)
            self.text.place(x=2, y=y)
            self.k = self.k + 1
            y += 20
        self.k1 = self.k
        self.vars1 = [StringVar() for _ in range(self.k1)]
        y1 = 10
        for i in range(self.k1):
            self.e = Entry(self, textvariable=self.vars1[i])
            self.e.place(x=300, y=y1)
            y1 += 20

        ###########################################
        self.vnestu = Button(self, text="Внести оцінки", font=15, command=self.add_ocinku)
        self.vnestu.place(x=400, y=y)
        self.vnestu.bind("<Button-1>")
        self.resizable(False, False)
        self.overrideredirect(False)

    def add_ocinku(self):
        global ocinku
        ocinku = [e.get() for e in self.vars1]
        for i1 in range(len(self.s1)):
            self.namber_z1 = self.s1[i1][0]
            print(self.namber_z1)
            cur3 = conn.cursor()
            db1 = (""" INSERT INTO Оцінки(Дата,Студенти_номер_залікової_книжки, оцінка,екзамен,предмет)
                  values(%s,%s,%s,%s,%s)""")
            z1 = (datetime.date(2018, 11, 3), self.namber_z1, int(ocinku[i1]), "Ekzamen", "pred")
            cur3.execute(db1, z1)
            cur3.close()
            conn.commit()
        if all(e1.get() != '' for e1 in self.vars1):
            print('Оценки проставлены')
        else:
            messagebox.showerror("Увага!", "Перевірте чи правельно введенні дані!")
        for e1 in self.vars1:
            e1.set('')

if __name__ == "__main__":
    root = tk.Tk()
    wind1 = Main(root)
    wind1.pack()

    root.geometry('700x600')
    root.config(bg='light blue')
    root.focus_set()
    root.grab_release()

    root.title('Помічник секретаря')
    leb1 = Label(root, text="Виберіть дію", font=25, bg='light blue')
    leb2 = Label(root, text=" ", font=30, bg='light blue')
    leb3 = Label(root, text=" ", font=30, bg='light blue')
    leb4 = Label(root, text=" ", font=30, bg='light blue')
    button1 = Button(root, text="Заповнити ", height=5, width=25, font=14, bg='light grey', command=Child)
    button2 = Button(root, text="Вивести дані", height=5, width=25, font=14, bg='light grey', command=Child8)
    button3 = Button(root, text="Внести зміни", height=5, width=25, font=14, bg='light grey', command=Child9)
    leb1.pack()
    leb4.pack()
    button1.pack()
    leb2.pack()
    button2.pack()
    leb3.pack()
    button3.pack()

    button1.bind("<Button-1>")
    button2.bind("<Button-1>")
    button3.bind("<Button-1>")
    root.overrideredirect(False)

    root.resizable(0, 0)
    root.mainloop()

conn.commit()
conn.close()