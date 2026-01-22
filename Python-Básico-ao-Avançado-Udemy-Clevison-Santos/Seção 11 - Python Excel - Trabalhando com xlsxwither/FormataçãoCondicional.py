import xlsxwriter as xls
import os

nomeCaminho = 'C:\\...\\imagem.xlsx'

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

workbook.close()

os.startfile(nomeCaminho)
