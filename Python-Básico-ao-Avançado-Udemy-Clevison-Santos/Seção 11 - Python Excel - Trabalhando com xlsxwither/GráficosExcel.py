import xlsxwriter as xls
import os

nomeCaminho = 'C:\\...\\Gráficos.xlsx'

workbook = xls.Workbook(nomeCaminho)
sheetDados = workbook.add_worksheet("Dados")

negrito = workbook.add_format({'bold': 1})

titulos = ['Vendedores', 'Total Vendas']
dadosTabela = [
    ['Ana', 'Pedro', 'Allan', 'Francisco', 'Rosa', 'Amanda'],
    [400, 300, 89, 34, 350, 120],
]

sheetDados.write_row('A1', titulos, negrito)
sheetDados.write_column('A2', dadosTabela[0])
sheetDados.write_column('B2', dadosTabela[1])

graficoColunas = workbook.add_chart({'type': 'column'})



workbook.close()

os.startfile(nomeCaminho)
