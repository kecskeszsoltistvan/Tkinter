from tkinter import *
ablak1 = Tk()
ablak1.title("IKT Projekt - 2022.03.16")
ablak1.geometry('300x200')
ablak1.maxsize(330, 200)
ablak1.minsize(330, 200)
icon = PhotoImage(file = "C:\\Users\\kecskeszsoltistvan\\Downloads\\hangman\\favicon.png")
ablak1.config(background="#eeeeee")
ablak1.iconphoto(True, icon)
kep1 = PhotoImage(file = "C:\\Users\\kecskeszsoltistvan\\Downloads\\hangman\\g.png")
Label(
    ablak1,
    text='Első mező:', 
    bg='#eeeeee'
).grid(row=0, column=0)

Label(
    ablak1,
    text='Második:',
    bg='#eeeeee'
).grid(row=1, column=0)

Label(
    ablak1,
    text='Harmadik:',
    bg='#eeeeee'
).grid(row=2, column=0)
Label(
    ablak1,
    bg='#eeeeee',
    image = kep1
).grid(row = 1, rowspan=1, column=2)

Entry(ablak1).grid(row=0, column=1)
Entry(ablak1).grid(row=1, column=1)
Entry(ablak1).grid(row=2, column=1)
ablak1.mainloop()
"""
Órai munka IG
"""