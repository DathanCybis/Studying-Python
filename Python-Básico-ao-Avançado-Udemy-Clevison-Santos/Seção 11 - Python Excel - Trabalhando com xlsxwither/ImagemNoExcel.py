import xlsxwriter as xls
import os

nomeCaminho = 'C:\\...\\imagem.xlsx'

workbook = xls.Workbook(nomeCaminho)
sheetDados = workbook.add_worksheet("Dados")


sheetDados.write("B3", "Imagem logo YT")

sheetDados.insert_image('B5', 'C:\\...\\.png')

workbook.close()

os.startfile(nomeCaminho)
