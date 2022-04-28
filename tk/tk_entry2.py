from tkinter import *

def massiv_print(mas, r, c):
    for x in range(r):
        for y in range(c):
            print(mas[y][x], end=' ')
        print()
    print()

def ent_change(x, y):
    massiv2[x][y] = ent_array2[x][y].get()
    massiv_print(massiv2, r, c)  # отладочный вывод


root = Tk()
frame = Frame(root)
frame.grid(row=0, column=0)

c = 8
r = 3
massiv2 = [[0 for x in range(r)] for x in range(c)]      # список для анализа
ent_array2 = [[0 for x in range(r)] for x in range(c)]   # список для кнопок

for x in range(c):
    for y in range(r):
        ent_array2[x][y] = Entry(frame)
        ent_array2[x][y].bind("<Enter>", ent_change(x, y))
        ent_array2[x][y].grid(column=x, row=y)

root.mainloop()

# namR = []
# for ii in range(0,20):
#     namR.append(Entry(master))
#     namR[ii].grid(row=2+ii, column=3)