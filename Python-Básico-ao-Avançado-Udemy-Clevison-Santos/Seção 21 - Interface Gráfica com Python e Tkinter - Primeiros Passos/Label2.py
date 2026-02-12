from tkinter import *

janela = Tk()

janela.title("Interface Gráfica / Label2")

texto = """Curso de Tkinter
Aprendendo como criar
Interface gráfica com
Python
"""

formato = Label(janela,
                font = "Arial 40 bold",
                text=texto).pack()

janela.mainloop() 
