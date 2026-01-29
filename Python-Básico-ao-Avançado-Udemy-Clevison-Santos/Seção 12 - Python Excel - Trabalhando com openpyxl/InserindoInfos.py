from openpyxl import load_workbook
import os
from openpyxl.styles import Color, PatternFill, Font, Border, Side
nomeCaminho = 'C:\\...\\InserirDadosPintarCelulas.xlsx'
planilha_aberta = load_workbook(filename=nomeCaminho)

sheet_selecionada = planilha_aberta['Professor']

dadosTabela = [
    ['Nome', 'Idade'],
    ['Berenice', 28],
    ['Caio', 32],
    ['Nicole', 34],
    ['Leonardo', 19],
    ['Amanda', 25]
]

for linha in dadosTabela:
    sheet_selecionada.append(linha)


corTitulo = PatterFill(start_color='00FFFF00')


planilha_aberta.save(filename=nomeCaminho)

os.startfile(nomeCaminho)
