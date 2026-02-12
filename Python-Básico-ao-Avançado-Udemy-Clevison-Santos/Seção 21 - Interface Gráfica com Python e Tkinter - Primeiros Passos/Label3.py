from tkinter import *

janela = Tk()

janela.title("Tela 3x3")

for linha in range(5):

    for coluna in range(3):

        tabela = Frame(

            master = janela,
            relief = RAISED,
            borderwidth=1

        )
        tabela.grid(row=linha, column=coluna)
        label = Label(master=tabela,
                      text=f"Linha {linha}\n Coluna {coluna}")
        label.pack()

janela.mainloop() 
