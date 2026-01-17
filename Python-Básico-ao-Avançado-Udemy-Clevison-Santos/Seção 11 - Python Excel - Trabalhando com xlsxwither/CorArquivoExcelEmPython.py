import xlsxwriter as xls
import os

nomeCaminho = '#caminho C:\\...\\...\\....xlsx'

workbook = xls.Workbook(nomeCaminho)
sheetPadrao = workbook.add_worksheet()


sheetPadrao.write("A1", "Nome")
sheetPadrao.write("B1", "Idade")
sheetPadrao.write("A2", "Amanda")
sheetPadrao.write("B2", 21)
sheetPadrao.write("A3", "Allan")
sheetPadrao.write("B3", 28)

workbook.close()

os.startfile(nomeCaminho)
