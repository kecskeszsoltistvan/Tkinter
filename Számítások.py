from tkinter import *
from tkinter import ttk
import math
def nevjegy():
    abl2 = Toplevel(ablak1)
    uz2 = Message(abl2, text="Készítette: Kecskés Zsolt\n2022.04.10", width=300)
    kilep = Button(abl2, text="Exit", command=abl2.destroy)
    uz2.pack()
    kilep.pack()
    abl2.mainloop()

def felszin1():
    def teszt():
        aa = float(a.get())
        bb = float(b.get())
        cc = float(c.get())
        hiba = False
        f = 2*(aa*bb+bb*cc+aa*cc)
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
            v1.delete(0, END)
            v1.insert(0, str(f))
    def Törlés():
        a.delete(0, END)
        b.delete(0, END)
        c.delete(0, END)
        v1.delete(0, END)
    fel = Toplevel(ablak1)
    fel.maxsize(220, 120)
    fel.minsize(220, 120)
    Label(
    fel,
    text='Hossz (cm):', 
    bg='#eeeeee'
    ).grid(row=0, column=0)

    Label(
    fel,
    text='Vastagság (cm):',
    bg='#eeeeee'
    ).grid(row=1, column=0)

    Label(
    fel,
    text='Szélesség (cm):',
    bg='#eeeeee'
    ).grid(row=2, column=0)

    a = ttk.Entry(fel)
    a.grid(row=0, column=1)
    b = ttk.Entry(fel)
    b.grid(row=1, column=1)
    c = ttk.Entry(fel)
    c.grid(row=2, column=1)
    gomb1 = Button(fel, text = "Kiszámít", command = teszt)
    gomb1.grid(row=3, column=0, sticky = "w") # Gomb
    gomb2 = Button(fel, text = "Töröl", command = Törlés)
    gomb2.grid(row=3, column=1, sticky = "e") # Gomb
    Label(
    fel,
    text='Felszín (cm²):',
    bg='#eeeeee'
    ).grid(row=4, column=0)
    v1 = Entry(fel)
    v1.grid(row=4, column=1)
    fel.mainloop()

def terfogat1():
    def teszt():
        aa = float(a.get())
        bb = float(b.get())
        cc = float(c.get())
        hiba = False
        f = aa*bb*cc
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
            v1.delete(0, END)
            v1.insert(0, str(f))
    def Törlés():
        a.delete(0, END)
        b.delete(0, END)
        c.delete(0, END)
        v1.delete(0, END)
    fel = Toplevel(ablak1)
    fel.maxsize(220, 120)
    fel.minsize(220, 120)
    Label(
    fel,
    text='Hossz (cm):', 
    bg='#eeeeee'
    ).grid(row=0, column=0)

    Label(
    fel,
    text='Vastagság (cm):',
    bg='#eeeeee'
    ).grid(row=1, column=0)

    Label(
    fel,
    text='Szélesség (cm):',
    bg='#eeeeee'
    ).grid(row=2, column=0)

    a = ttk.Entry(fel)
    a.grid(row=0, column=1)
    b = ttk.Entry(fel)
    b.grid(row=1, column=1)
    c = ttk.Entry(fel)
    c.grid(row=2, column=1)
    gomb1 = Button(fel, text = "Kiszámít", command = teszt)
    gomb1.grid(row=3, column=0, sticky = "w") # Gomb
    gomb2 = Button(fel, text = "Töröl", command = Törlés)
    gomb2.grid(row=3, column=1, sticky = "e") # Gomb
    Label(
    fel,
    text='Térfogat (cm³):',
    bg='#eeeeee'
    ).grid(row=4, column=0)
    v1 = Entry(fel)
    v1.grid(row=4, column=1)
    fel.mainloop()

def felszin2():
    def teszt():
        aa = float(a.get())
        bb = float(b.get())
        hiba = False
        f = 2 * aa ** 2 * math.pi + 2 * aa * math.pi * bb
        if aa <= 0:
           a.delete(0, END)
           a.insert(0, "Érvénytelen adat!")
           hiba = True
        if bb <= 0:
            b.delete(0, END)
            b.insert(0, "Érvénytelen adat!")
            hiba = True
        if hiba == True:
            return None
        else:
            v1.delete(0, END)
            v1.insert(0, str(f))
    def Törlés():
        a.delete(0, END)
        b.delete(0, END)
        c.delete(0, END)
        v1.delete(0, END)
    fel = Toplevel(ablak1)
    fel.maxsize(220, 120)
    fel.minsize(220, 120)
    Label(
    fel,
    text='Radius (cm):', 
    bg='#eeeeee'
    ).grid(row=0, column=0)

    Label(
    fel,
    text='Magasság (cm):',
    bg='#eeeeee'
    ).grid(row=1, column=0)

    a = ttk.Entry(fel)
    a.grid(row=0, column=1)
    b = ttk.Entry(fel)
    b.grid(row=1, column=1)
    gomb1 = Button(fel, text = "Kiszámít", command = teszt)
    gomb1.grid(row=2, column=0, sticky = "w") # Gomb
    gomb2 = Button(fel, text = "Töröl", command = Törlés)
    gomb2.grid(row=2, column=1, sticky = "e") # Gomb
    Label(
    fel,
    text='Felszín (cm²):',
    bg='#eeeeee'
    ).grid(row=3, column=0)
    v1 = Entry(fel)
    v1.grid(row=3, column=1)
    fel.mainloop()

def terfogat2():
    def teszt():
        aa = float(a.get())
        bb = float(b.get())
        hiba = False
        f = aa ** 2 * math.pi * bb
        if aa <= 0:
           a.delete(0, END)
           a.insert(0, "Érvénytelen adat!")
           hiba = True
        if bb <= 0:
            b.delete(0, END)
            b.insert(0, "Érvénytelen adat!")
            hiba = True
        if hiba == True:
            return None
        else:
            v1.delete(0, END)
            v1.insert(0, str(f))
    def Törlés():
        a.delete(0, END)
        b.delete(0, END)
        c.delete(0, END)
        v1.delete(0, END)
    fel = Toplevel(ablak1)
    fel.maxsize(220, 120)
    fel.minsize(220, 120)
    Label(
    fel,
    text='Radius (cm):', 
    bg='#eeeeee'
    ).grid(row=0, column=0)

    Label(
    fel,
    text='Magasság (cm):',
    bg='#eeeeee'
    ).grid(row=1, column=0)

    a = ttk.Entry(fel)
    a.grid(row=0, column=1)
    b = ttk.Entry(fel)
    b.grid(row=1, column=1)
    gomb1 = Button(fel, text = "Kiszámít", command = teszt)
    gomb1.grid(row=2, column=0, sticky = "w") # Gomb
    gomb2 = Button(fel, text = "Töröl", command = Törlés)
    gomb2.grid(row=2, column=1, sticky = "e") # Gomb
    Label(
    fel,
    text='Felszín (cm²):',
    bg='#eeeeee'
    ).grid(row=3, column=0)
    v1 = Entry(fel)
    v1.grid(row=3, column=1)
    fel.mainloop()

ablak1 = Tk()
ablak1.title("IKT Projekt - Szenvedés - 2022.04.06")
ablak1.geometry('220x100')
ablak1.maxsize(300, 100)
ablak1.minsize(300, 100)
icon = PhotoImage(file = "C:\\Users\\kecskeszsoltistvan\\Downloads\\Tkinter-main\\g.png")
ablak1.config(background="#eeeeee")
ablak1.iconphoto(True, icon)

ms = Frame(ablak1)
ms.pack(side = TOP, fill = X)

m1 = Menubutton(ms, text = "Fájl", underline = 0)
m1.pack(side = LEFT)
fm = Menu(m1)
fm.add_command(label="Névjegy",command=nevjegy, underline = 0)
fm.add_command(label="Kilépés",command=ablak1.destroy, underline = 0)
m1.config(menu = fm)
m2 = Menubutton(ms, text="Téglatest számítások", underline = 0)
m2.pack(side = LEFT)
tm = Menu(m2)
tm.add_command(label="Felszín",command=felszin1, underline = 0)
tm.add_command(label="Térfogat",command=terfogat1, underline = 0)
m2.config(menu = tm)
m3 = Menubutton(ms, text="Henger számítások", underline = 0)
m3.pack(side = LEFT)
tm = Menu(m3)
tm.add_command(label="Felszín",command=felszin2, underline = 0)
tm.add_command(label="Térfogat",command=terfogat2, underline = 0)
m3.config(menu = tm)
ablak1.mainloop()