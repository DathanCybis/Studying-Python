import xlsxwriter as xls
import os

nomeCaminho = 'C:\\...\\...\\MergeCells.xlsx'

workbook = xls.Workbook(nomeCaminho)
sheetDados = workbook.add_worksheet("MergeCells")

add_merge = workbook.add_format({
    'bold': True,
    'border': 6,
    'valign':'vcemter',
    'size':30,
    'fg_color':'blue',
    'font_color':'white'
})

sheetDados.merge_range('B3:I5', 'Merge Células', add_merge)

workbook.close()

os.startfile(nomeCaminho)
