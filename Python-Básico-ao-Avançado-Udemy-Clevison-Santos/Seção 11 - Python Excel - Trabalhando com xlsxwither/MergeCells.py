import xlsxwriter as xls
import os

nomeCaminho = 'C:\\...\\...\\Formulas.xlsx'

workbook = xls.Workbook(nomeCaminho)
sheetDados = workbook.add_worksheet("Dados")

add_merge = workbook.add_format({
    'bold:' True,
    'border': 6,
    'valign':'vcemter',
    'size':30,
    'fg_color':'blue',
    'font_color':'white'

})

workbook.close()

os.startfile(nomeCaminho)
