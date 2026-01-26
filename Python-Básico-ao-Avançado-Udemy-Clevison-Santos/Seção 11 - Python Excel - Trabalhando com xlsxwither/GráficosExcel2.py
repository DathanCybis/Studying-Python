import xlsxwriter as xls
import os

nomeCaminho = 'C:\\...\\Gráficos2.xlsx'

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

graficoColunas.add_series({
    'name': '=Resumo!$B$1',
    'categories': '=Resumo!$A$2:$A$7',
    'values': '=Resumo!$B$2:$B$7'
})

graficoColunas.set_title({'name': 'Gráfico total de vendas'})
graficoColunas.set_x_axis({'name': 'Vendedores'})
graficoColunas.set_y_axis({'name': 'Vendas'})

graficoColunas.set_style(11)

sheetDados.insert_chart('D2', graficoColunas, {'x_offset': 25, 'y_offset': 10})

##############################################################

graficoEmpilhado = workbook.add_chart({'type': 'area', 'subtype': 'stacked'})

graficoEmpilhado.add_series({
    'name': '=Resumo!$B$1',
    'categories': '=Resumo!$A$2:$A$7',
    'values': '=Resumo!$B$2:$B$7'
})

graficoEmpilhado.set_title({'name': 'Gráfico Empilhado'})
graficoEmpilhado.set_x_axis({'name': 'Funcionarios'})
graficoEmpilhado.set_y_axis({'name': 'Vendas'})

graficoEmpilhado.set_style(12)

sheetDados.insert_chart('L2', graficoEmpilhado, {'x_offset': 25, 'y_offset': 10})

workbook.close()

os.startfile(nomeCaminho) 
