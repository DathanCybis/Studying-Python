import xlsxwriter as xls
import os

nomeCaminho = 'C:\\..'

workbook = xls.Workbook(nomeCaminho)
sheetDados = workbook.add_worksheet("Dados")


sheetDados.write("B3", "Imagem")

sheetDados.insert_image('B5', '')