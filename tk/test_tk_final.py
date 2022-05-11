from tkinter import *
from tkinter import messagebox

def changeBut(event, button):
    i, j = button["text"].split('_')
    i = int(i)
    j = int(j)
    # if button.cget("bg") == "white":
    if button["bg"] == "white":
        button.configure(bg="black")
        button.configure(fg="black")
        mas[i][j] = 1
    else:
        button.configure(bg="white")
        button.configure(fg="white")
        mas[i][j] = 0
    for i in range(l):
        print(mas[i])

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


root = Tk()
root.title("Создание японского кроссворда")
l = 5

mas = [0] * l
parY = [[]] * l
parX = [[]] * l

for i in range(l):
    mas[i] = [0] * l
for i in range(l):
    print(mas[i])

Label(root, text='Здравствуйте! Для создания своего японского кроссворда нужно:', font='Arial 16').grid(column=0, row=0)
Label(root, text='1. Нарисовать нужный рисунок на поле.', font='Arial 12').grid(column=0, row=1)
Label(root, text='2. Заполнить параметры, находящиеся слева и сверху от поля.', font='Arial 12').grid(column=0, row=2)
Label(root, text='Если групп несколько, то вводите параметры через пробел.', font='Arial 12').grid(column=0, row=3)
Label(root, text='Например: если в первой строке мы закрасим 2 группы клеток, в каждой из которых 3 клетки,', font='Arial 12').grid(column=0, row=4)
Label(root, text='в параметре нужно написать: "3 3"', font='Arial 12').grid(column=0, row=5)
Label(root, text='3. После ввода параметров нажмите клавишу Enter!', font='Arial 12').grid(column=0, row=6)
Label(root, text='3. Когда все заполнено, нажмите кнопку "Проверка".', font='Arial 12').grid(column=0, row=7)

for i in range(l):
    for j in range(l):
        but = Button(root,
                     height=3,
                     width=7,
                     borderwidth=1,
                     bg="white",
                     fg="white")
        but["text"] = str(i) + "_" + str(j)
        but.bind("<Button-1>", lambda event, but=but: changeBut(event, but))
        but.grid(row=i+1, column=j+2)

arrayY1 = [0] * l
arrayY2 = [0] * l

arrayX1 = [0] * l
arrayX2 = [0] * l

for i in range(l):
    arrayY1[i] = Entry(root, width=7,bd=5)
    arrayX1[i] = Entry(root, width=7,bd=5)

    arrayY1[i].bind('<Return>', Save)
    arrayX1[i].bind('<Return>', Save)

    arrayY1[i].grid(row=i+1, column=1)
    arrayX1[i].grid(row=0, column=i+2)

print(arrayY1)

CheckButton = Button(root, text="Проверка", bg = '#eb958f', command=checker)
CheckButton.grid(row=20, column = 1)



root.mainloop()
