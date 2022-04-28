from tkinter import *

def massiv_print():
    for x in range(r):
        for y in range(c):
            print(massiv[y][x], end=' ')
        print()
    print()

def color_change(x,y):
    if btn_array[x][y]["bg"] == "white":
        btn_array[x][y].config(bg="black")
    else:
        btn_array[x][y].config(bg="white")
    if massiv[x][y] == 0:
        massiv[x][y] = 1
    else:
        massiv[x][y] = 0
    massiv_print()  # отладочный вывод


root = Tk()
frame = Frame(root)
frame.grid(row=0,column=0)

c = 8
r = 6
massiv = [[0 for x in range(r)] for x in range(c)]      # список для анализа
btn_array = [[0 for x in range(r)] for x in range(c)]   # список для кнопок

for x in range(c):
    for y in range(r):
        btn_array[x][y] = Button(frame,
                                 bg="white",
                                 height=1, width=2,
                                 command= lambda x1=x, y1=y: color_change(x1,y1))
        btn_array[x][y].grid(column=x, row=y)

root.mainloop()

