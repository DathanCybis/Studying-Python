import xlsxwriter as xls
import os

nomeCaminho = 'C:\\...\\Condicional.xlsx'

workbook = xls.Workbook(nomeCaminho)
sheetDados = workbook.add_worksheet("Dados")


formatoMaior = workbook.add_format({
    'bg_color': 'green',
    'fort_color': 'white'
})
formatoMenor = workbook.add_format({
    'bg_color': 'red',
    'fort_color': 'white'
})

inserirDados = [
    ["Coluna 1", "Coluna 2", "Coluna 3", "Coluna 4"],
    [34, 25, 64, 32],
    [92, 72, 11, 3],
    [37, 56, 87, 22],
    [7, 49, 51, 99]
]

workbook.close()

os.startfile(nomeCaminho)
