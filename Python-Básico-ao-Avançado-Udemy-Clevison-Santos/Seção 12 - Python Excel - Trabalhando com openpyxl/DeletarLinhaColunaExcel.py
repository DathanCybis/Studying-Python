import xlsxwriter as xls
import os

nomeCaminho = 'C:\\...\\DeletarLinhaColunaExcel.xlsx'

workbook = xls.Workbook(nomeCaminho)
sheetDados = workbook.add_worksheet("Dados")




workbook.close()

os.startfile(nomeCaminho) 
