from tkinter import *
from tkinter import ttk

def nevjegy():
    abl2 = Toplevel(ablak1)
    uz2 = Message(abl2, text="Készítette: Gipsz Jakab\n2022.04.05", width=300)
    kilep = Button(abl2, text="Exit", command=abl2.destroy)
    uz2.pack()
    kilep.pack()
    abl2.mainloop()

def felszin():
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
            abl2 = Toplevel(ablak1)
            abl2.maxsize(210, 50)
            abl2.minsize(210, 50)
            abl2.title("Eredmények")
            Label(
            abl2,
            text='Felszín (cm²):',
            bg='#eeeeee'
            ).grid(row=1, column=0)
            v1 = Entry(abl2)
            v1.grid(row=1, column=1)
            v1.delete(0, END)
            v1.insert(0, str(f))
            abl2.mainloop()
    fel = Toplevel(ablak1)
    fel.maxsize(220, 100)
    fel.minsize(220, 100)
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
    gomb = Button(fel, text = "Kiszámít", command = teszt)
    gomb.grid(row=3, column=0, sticky = "w") # Gomb
    fel.mainloop()

def terfogat():
    def teszt():
        aa = float(a.get())
        bb = float(b.get())
        cc = float(c.get())
        hiba = False
        f = (a*b*c)
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
            text='Térfogat (cm²):',
            bg='#eeeeee'
            ).grid(row=1, column=0)
            v1 = Entry(abl2)
            v1.grid(row=1, column=1)
            v1.delete(0, END)
            v1.insert(0, str(f))
            abl2.mainloop()
    fel = Toplevel(ablak1)
    fel.maxsize(220, 100)
    fel.minsize(220, 100)
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
    gomb = Button(fel, text = "Kiszámít", command = teszt)
    gomb.grid(row=3, column=0, sticky = "w") # Gomb
    fel.mainloop()

"""
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



"""

ablak1 = Tk()
ablak1.title("IKT Projekt - Szenvedés - 2022.04.06")
ablak1.geometry('220x100')
ablak1.maxsize(220, 100)
ablak1.minsize(220, 100)
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
tm.add_command(label="Felszín",command=felszin, underline = 0)
tm.add_command(label="Térfogat",command=terfogat, underline = 0)
m2.config(menu = tm)
ablak1.mainloop()