from tkinter import *

janela = Tk()

janela.title("Interface Gráfica")

intrucao = Label(text="Bem vindos ao Curso de Tkinter")

intrucao.pack()

intrucao2 = Label(text="Interface Gráfica")

intrucao2.pack()

r1 = Label(janela, text = "FLAT", relief=FLAT)
r2 = Label(janela, text = "RAISED", relief=RAISED)
r3 = Label(janela, text = "SUNKEN", relief=SUNKEN)
r4 = Label(janela, text = "GROOVE", relief=GROOVE)
r5 = Label(janela, text = "RIDGE", relief=RIDGE)

r1.pack()
r2.pack()
r3.pack()
r4.pack()
r5.pack()

r1 = Label(janela, text = "FLAT BG FG FONT", relief=FLAT, bg="green", fg="white", font="arial")
r1.pack()

r4 = Label(janela, text = "GROOVE borderwidth", relief=GROOVE, bg="green", fg="white", borderwidth=10)
r4.pack()

janela.mainloop() 
