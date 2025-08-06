from tkinter import *
import os

def abrirCalculadora():
    os.system("calc")

def abrirChrome ():
    os.system("start chrome")

ventana = Tk()
ventana.title("Menú principal")
ventana.config(bg="yellow")
ventana.geometry("520x480")
ventana.resizable(0,0)

botonCalc = Button(text="calculadora", command=abrirCalculadora)
botonCalc.place(x= 50, y=50)
bontonChrome = Button(text="⚔chrome", command=abrirChrome)
bontonChrome.place(x=125,y=50)

ventana.mainloop()