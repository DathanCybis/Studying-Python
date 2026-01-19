import xlsxwriter as xls
import os

nomeCaminho = 'C:\\...\\...\\pintafundoefonte.xlsx'

workbook = xls.Workbook(nomeCaminho)
sheetDados = workbook.add_worksheet("Dados")

corFundo = workbook.add_format({"fg_color":'yellow'})

corFonte = workbook.add_format()
corFonte.set_font_color('blue')

sheetDados.write("A1", "Nome", corFundo)
sheetDados.write("B1", "Idade", corFundo)
sheetDados.write("A2", "Amanda", corFonte)
sheetDados.write("B2", 21, corFonte)
sheetDados.write("A3", "Allan", corFonte)
sheetDados.write("B3", 28, corFonte)

workbook.close()

os.startfile(nomeCaminho) 
