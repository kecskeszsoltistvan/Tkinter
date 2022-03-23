from tkinter import *
from tkinter import ttk
import math

def teszt():
    
    radius = int(r.get())
    mass = int(m.get())
    V = radius ** 2 * mass * math.pi
    Vas = V * 7,874
    Vfa = V * 0.650
    v.delete(0, END)
    v.insert(0, V)
    v1.delete(0, END)
    v1.insert(0, Vas)
    v2.delete(0, END)
    v2.insert(0, Vfa)
    return None

ablak1 = Tk()
ablak1.title("IKT Projekt - Vashenger - 2022.03.22")
ablak1.geometry('220x140')
ablak1.maxsize(220, 140)
ablak1.minsize(220, 140)
icon = PhotoImage(file = "C:\\Users\\kecskeszsoltistvan\\Downloads\\Tkinter-main\\favicon.png")
ablak1.config(background="#eeeeee")
ablak1.iconphoto(True, icon)
Label(
    ablak1,
    text='Sugár (cm):', 
    bg='#eeeeee'
).grid(row=0, column=0)

Label(
    ablak1,
    text='Magasság (cm):',
    bg='#eeeeee'
).grid(row=1, column=0)

Label(
    ablak1,
    text='Térfogat:',
    bg='#eeeeee'
).grid(row=3, column=0)

Label(
    ablak1,
    text='Vashenger:',
    bg='#eeeeee'
).grid(row=4, column=0)

Label(
    ablak1,
    text='Fahenger:',
    bg='#eeeeee'
).grid(row=5, column=0)

r = ttk.Entry(ablak1)
r.grid(row=0, column=1)
m = ttk.Entry(ablak1)
m.grid(row=1, column=1)



gomb = Button(ablak1, text = "Kiszámít", command = teszt).grid(row=2, column=1, sticky = "e")

v = Entry(ablak1)
v.grid(row=3, column=1)
v1 = Entry(ablak1)
v1.grid(row=4, column=1)
v2 = Entry(ablak1)
v2.grid(row=5, column=1)
ablak1.mainloop()
"""
Órai munka IG
"""