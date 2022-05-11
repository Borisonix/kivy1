from tkinter import *
# from tkinter.ttk import *
from tkinter import messagebox

# глобальные переменные
l = 5
c = 5
r = 5


class Application(Frame):
    def __init__ (self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.master.title("Создание японского кроссворда")
        self.master.resizable(False, False)


    def create_widgets(self):
        self.massiv = [[0 for x in range(r)] for x in range(c)]  # список для анализа
        self.btn_array = [[0 for x in range(r)] for x in range(c)]  # список для кнопок

        for x in range(c):
            for y in range(r):
                self.btn_array[x][y] = Button(self,
                                         bg="white",
                                         height=1, width=2,
                                         command=lambda x1=x, y1=y: self.color_change(self, x1, y1))
                self.btn_array[x][y].grid(column=x, row=y)

    def color_change(self, x, y):
        if self.btn_array[x][y]["bg"] == "white":
            self.btn_array[x][y].config(bg="black")
        else:
            self.btn_array[x][y].config(bg="white")
        if self.massiv[x][y] == 0:
            self.massiv[x][y] = 1
        else:
            self.massiv[x][y] = 0
        # massiv_print()  # отладочный вывод

"""
    def Save(event):
        for i in range(l):
            arrayY2[i] = arrayY1[i].get()
            arrayX2[i] = arrayX1[i].get()
        print(arrayY2, arrayX2)

        for j in range(l):
            arrayY2[j].strip()
            c = []
            if arrayY2[j] == '10':
                parY[j] = [10]
                continue
            for i in range(len(arrayY2[j])):
                if arrayY2[j][i] != ' ':
                    if len(arrayY2[j]) == 1:
                        parY[j] = [int(arrayY2[j])]
                        break
                    c.append(int(arrayY2[j][i]))
                    continue
                else:
                 parY[j] = c
                 continue
                parY[j] = c

        for j in range(l):
            arrayX2[j].strip()
            c = []
            if arrayX2[j] == '10':
                parX[j] = [10]
                continue
            for i in range(len(arrayX2[j])):
                if arrayX2[j][i] != ' ':
                    if len(arrayX2[j]) == 1:
                        parX[j] = [int(arrayX2[j])]
                        break
                    c.append(int(arrayX2[j][i]))
                    continue
                else:
                 parX[j] = c
                 continue
                parX[j] = c
        print(parY, parX)

    def kolvo_group(row,n):
        if row:
            x1 = mas[n][0:l]
        else:
            x1 = []
            for i in range(l):
                x1.append(mas[i][n])
        x2 = list(map(str,x1))
        x3 = ''.join(x2)
        x4 = x3.replace('0',' ')
        x5 = x4.split()                     # группы черных квадратов
        kg = len(x5)                        # кол-во групп черных квадратов
        x6 = list(map(len, x5))             # длины групп
        k = x3.count('1')                   # кол-во черных квадратов
        return kg, k, x6

    def checker():
        error = False
        for i in range(l):
            kg, k, x6 = kolvo_group(True, i)
            kY = sum(parY[i])
            kgY = len(parY[i])
            if k == kY and kg != kgY:
                error = True
                messagebox.showinfo('Ошибка', f'В ряду {i+1} между группами нет разделителя!')
            elif kg != kgY:
                error = True
                messagebox.showinfo('Ошибка', f'В ряду {i+1} не совпадает количество групп!')
            else:
                if x6 != parY[i]:
                    error = True
                    messagebox.showinfo('Ошибка', f'В ряду {i+1} неверное количество клеток в одной из групп!')

            for i in range(l):
                kg, k, x6 = kolvo_group(False, i)
                kX = sum(parX[i])
                kgX = len(parX[i])
                if k == kX and kg != kgX:
                    error = True
                    messagebox.showinfo('Ошибка', f'В колонке {i+1} между группами нет разделителя!')
                elif kg != kgX:
                    error = True
                    messagebox.showinfo('Ошибка', f'В колонке {i+1} не совпадает количество групп!')
                else:
                    if x6 != parX[i]:
                        error = True
                        messagebox.showinfo('Ошибка', f'В колонке {i+1} неверное количество клеток в одной из групп!')
            if not error:
                messagebox.showinfo('Успех', 'Все правильно!')
"""

if __name__ == "__main__":
    root = Tk()
    app = Application(master=root)

    root.mainloop()
