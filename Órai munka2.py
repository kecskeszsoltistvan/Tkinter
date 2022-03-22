from tkinter import *
import math
ablak1 = Tk()
ablak1.title("IKT Projekt - Vashenger- 2022.03.22")
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

r = Entry(ablak1).grid(row=0, column=1)
m = Entry(ablak1).grid(row=1, column=1)

def teszt():
    v.delete(0, END)
    return None

gomb = Button(ablak1, text ="Hello", ).grid(row=2, column=1)
Valami = "asd"
v = Entry(ablak1,state='disabled',textvariable=Valami).grid(row=3, column=1)
v1 = Entry(ablak1,state='disabled',textvariable=Valami).grid(row=4, column=1)
v2 = Entry(ablak1,state='disabled',textvariable=Valami).grid(row=5, column=1)
ablak1.mainloop()
"""
Órai munka IG
"""