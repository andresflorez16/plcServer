from tkinter import *
import tkinter

def verifyIP():
    if inputIP.get():
        checkLblIP["text"] = '✅'
        checkLblIP.config(foreground='green')
        inputIP.config(state="disabled")
        btn.place_forget()
        lbl2.place(x=0, y=100)
        inputTagName.place(x=180, y=100)
    else:
        checkLblIP["text"] = 'Type a correct IP direction'
        checkLblIP.config(foreground='red')

ventana = tkinter.Tk()

ventana.title("PLC Server")
ventana.geometry("500x400")
ventana.resizable(width=False, height=False)

title = Label(ventana,text="PLC Server", bg="#222", foreground="#fff", font="Monospace 30")
title.pack(fill= tkinter.X)

lbl = Label(ventana,text="Please type IP direction:", font="Monospace 10")
lbl.place(x=0, y=70)

checkLblIP= Label(ventana, font="Monospace 10")
checkLblIP.place(x=300, y=70)

lbl2 = Label(ventana,text="Please type the variable Tag:", font="Monospace 10")
lbl2.place_forget()

inputIP = Entry(ventana, highlightthickness=2, highlightcolor="#000", highlightbackground="#000", font="Monospace 10")
inputIP.place(x=150, y=70)

inputTagName = Entry(ventana, highlightthickness=2, highlightcolor="#000", highlightbackground="#000", font="Monospace 10")
inputTagName.place_forget()

btn = Button(ventana, text="Presionar", highlightthickness=2, highlightcolor="#000", highlightbackground="#000", font="Monospace 10", command = verifyIP)
btn["fg"]="#000"
btn["bg"]="#8aedd3"
btn.place(x=1, y=100, width=70, height=25)


ventana.mainloop()
