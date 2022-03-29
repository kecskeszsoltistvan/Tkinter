from tkinter import *
from tkinter import ttk
import math
def teszt():
    radius = float(r.get())
    mass = float(m.get())
    liter = float(l.get())
    hiba = False
    V = radius ** 2 * mass * math.pi
    if liter <= 0:
        v.delete(0, END)
        v1.delete(0, END)
        v2.delete(0, END)
        l.delete(0, END)
        l.insert(0, "Érvénytelen adat!")
        hiba = True
    if mass <= 0:
        v.delete(0, END)
        v1.delete(0, END)
        v2.delete(0, END)
        m.delete(0, END)
        m.insert(0, "Érvénytelen adat!")
        hiba = True
    if radius <= 0:
        v.delete(0, END)
        v1.delete(0, END)
        v2.delete(0, END)
        r.delete(0, END)
        r.insert(0, "Érvénytelen adat!")
        hiba = True
    if hiba == True:
        return None
    if V > liter * 1000:
        v1.delete(0, END)
        v1.insert(0, "Igen.")
        Sz = ((liter / V) * 100) * 1000
        v.delete(0, END)
        v.insert(0, V)
        v2.delete(0, END)
        v2.insert(0, Sz)
    else:
        v1.delete(0, END)
        v1.insert(0, "Nem.")
        v.delete(0, END)
        v2.delete(0, END)
    return None

ablak1 = Tk()
ablak1.title("IKT Projekt - Hordószámítás - 2022.03.29")
ablak1.geometry('256x160')
ablak1.maxsize(256, 160)
ablak1.minsize(256, 160)
icon = PhotoImage(file = "C:\\Users\\kecskeszsoltistvan\\Downloads\\Tkinter-main\\g.png")
ablak1.config(background="#eeeeee")
ablak1.iconphoto(True, icon)
Label(
    ablak1,
    text='Hordó Sugár (cm):', 
    bg='#eeeeee'
).grid(row=0, column=0)

Label(
    ablak1,
    text='Hordó Magasság (cm):',
    bg='#eeeeee'
).grid(row=1, column=0)

Label(
    ablak1,
    text='Bor tartalom (l):',
    bg='#eeeeee'
).grid(row=2, column=0)

Label(
    ablak1,
    text='Térfogat (cm³):',
    bg='#eeeeee'
).grid(row=4, column=0)

Label(
    ablak1,
    text='Belefér:',
    bg='#eeeeee'
).grid(row=5, column=0)

Label(
    ablak1,
    text='Fahenger:',
    bg='#eeeeee'
).grid(row=6, column=0)
r = ttk.Entry(ablak1)
r.grid(row=0, column=1)
m = ttk.Entry(ablak1)
m.grid(row=1, column=1)
l = ttk.Entry(ablak1)
l.grid(row=2, column=1)
gomb = Button(ablak1, text = "Kiszámít", command = teszt).grid(row=3, column=1, sticky = "e") # Gomb
v = Entry(ablak1)
v.grid(row=4, column=1)
v1 = Entry(ablak1)
v1.grid(row=5, column=1)
v2 = Entry(ablak1)
v2.grid(row=6, column=1)
ablak1.mainloop()