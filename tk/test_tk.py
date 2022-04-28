from tkinter import *


def changeBut(event, button):
    # if button.cget("bg") == "white":
    if button["bg"] == "white":
        button.configure(bg="black")
        button.configure(fg="black")
    else:
        button.configure(bg="white")
        button.configure(fg="white")
    i, j = button["text"].split('_')
    print(i, j)
    attrs = []
    for key in sorted(button.__dict__):
        attrs.append('%s=%s' % (key, getattr(button, key)))
    print(', '.join(attrs))



root = Tk()

for i in range(10):
    for j in range(10):
        but = Button(root,
                     borderwidth=1,
                     bg="white",
                     fg="white")
        but["text"] = str(i) + "_" + str(j)
        but.bind("<Button-1>", lambda event, but=but: changeBut(event, but))
        but.grid(row=i, column=j)

root.mainloop()
