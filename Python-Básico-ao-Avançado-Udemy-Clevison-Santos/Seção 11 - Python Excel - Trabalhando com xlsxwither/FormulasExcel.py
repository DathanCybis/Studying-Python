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
sheetDados.write("A5", 2)
sheetDados.write("A8", "Ana")

sheetDados.write("B2", 9)
sheetDados.write("B3", 5)
sheetDados.write("B4", 7)
sheetDados.write("B5", 3)
sheetDados.write("B8", "Paula")

sheetDados.write("C2", "=A2+B2")
sheetDados.write("C3", "=A3-B3")
sheetDados.write("C4", "=A4*B4")
sheetDados.write("C5", "=A5/B5")
sheetDados.write("C8", '=CONCATENATE(A8," ",B8)')

workbook.close()

os.startfile(nomeCaminho)
