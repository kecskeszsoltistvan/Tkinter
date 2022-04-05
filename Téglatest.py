from tkinter import *
from tkinter import ttk
import math
def teszt():
    aa = float(a.get())
    bb = float(b.get())
    cc = float(c.get())
    hiba = False
    f = 2*(aa*bb+bb*cc+aa*cc)
    t = aa*bb*cc
    if aa <= 0:
        a.delete(0, END)
        a.insert(0, "Érvénytelen adat!")
        hiba = True
    if bb <= 0:
        b.delete(0, END)
        b.insert(0, "Érvénytelen adat!")
        hiba = True
    if cc <= 0:
        c.delete(0, END)
        c.insert(0, "Érvénytelen adat!")
        hiba = True
    if hiba == True:
        return None
    else:
        abl2 = Toplevel(ablak1)
        abl2.maxsize(210, 50)
        abl2.minsize(210, 50)
        abl2.title("Eredmények")
        Label(
        abl2,
        text='Térfogat (cm³):',
        bg='#eeeeee'
        ).grid(row=0, column=0)

        Label(
        abl2,
        text='Felszín (cm²):',
        bg='#eeeeee'
        ).grid(row=1, column=0)
        v = Entry(abl2)

        v.grid(row=0, column=1)

        v1 = Entry(abl2)

        v1.grid(row=1, column=1)

        v.delete(0, END)
        v.insert(0, str(t))
        v1.delete(0, END)
        v1.insert(0, str(f))
        abl2.mainloop()

ablak1 = Tk()
ablak1.title("IKT Projekt - Hordószámítás - 2022.03.29")
ablak1.geometry('256x160')
ablak1.maxsize(220, 100)
ablak1.minsize(220, 100)
icon = PhotoImage(file = "C:\\Users\\kecskeszsoltistvan\\Downloads\\Tkinter-main\\g.png")
ablak1.config(background="#eeeeee")
ablak1.iconphoto(True, icon)
Label(
    ablak1,
    text='Hossz (cm):', 
    bg='#eeeeee'
).grid(row=0, column=0)

Label(
    ablak1,
    text='Vastagság (cm):',
    bg='#eeeeee'
).grid(row=1, column=0)

Label(
    ablak1,
    text='Szélesség (cm):',
    bg='#eeeeee'
).grid(row=2, column=0)

a = ttk.Entry(ablak1)
a.grid(row=0, column=1)
b = ttk.Entry(ablak1)
b.grid(row=1, column=1)
c = ttk.Entry(ablak1)
c.grid(row=2, column=1)
gomb = Button(ablak1, text = "Kiszámít", command = teszt).grid(row=3, column=1, sticky = "e") # Gomb

ablak1.mainloop()