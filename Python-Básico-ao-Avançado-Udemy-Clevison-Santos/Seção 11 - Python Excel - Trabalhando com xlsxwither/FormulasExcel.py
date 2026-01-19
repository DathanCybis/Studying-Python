import xlsxwriter as xls
import os

nomeCaminho = 'C:\\...\\...\\Formulas.xlsx'

workbook = xls.Workbook(nomeCaminho)
sheetDados = workbook.add_worksheet("Dados")

corFundo = workbook.add_format({"fg_color":'yellow'})

corFonte = workbook.add_format()
corFonte.set_font_color('blue')

sheetDados.write("A1", "Número1")
sheetDados.write("B1", "Número2")
sheetDados.write("C1", "Fórmula")

sheetDados.write("A2", 10)
sheetDados.write("A3", 6)
sheetDados.write("A4", 8)

sheetDados.write("B2", 9)
sheetDados.write("B3", 5)
sheetDados.write("B4", 7)

workbook.close()

os.startfile(nomeCaminho) 

