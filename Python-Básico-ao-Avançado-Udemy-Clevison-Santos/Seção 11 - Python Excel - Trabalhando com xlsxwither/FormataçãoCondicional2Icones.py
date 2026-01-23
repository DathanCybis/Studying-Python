import xlsxwriter as xls
import os

nomeCaminho = 'C:\\...\\CondicionalIcones.xlsx'

workbook = xls.Workbook(nomeCaminho)
sheetDados = workbook.add_worksheet("Dados")


inserirDados = [
    ["Coluna 1", "Coluna 2", "Coluna 3", "Coluna 4"],
    [34, 25, 64, 32],
    [92, 72, 11, 3],
    [37, 56, 87, 22],
    [7, 49, 51, 99]
]

sheetDados.write('A1', "Formatação condicional com icones")

for linha, range in enumerate(inserirDados):
    sheetDados.write_row(linha + 2, 1, range)


sheetDados.conditional_format('B4:E7', {'type': 'icon_set',
                                        'icon_style': '3_traffic_lights'})

sheetDados.conditional_format('B4:E7', {'type': 'icon_set',
                                        'icon_style': '3_traffic_lights',
                                        'reverse_icons': True})

sheetDados.conditional_format('B4:E7', {'type': 'icon_set',
                                        'icon_style': '3_arrows'})

sheetDados.conditional_format('B4:E7', {'type': 'icon_set',
                                        'icon_style': '4_arrows'})

sheetDados.conditional_format('B4:E7', {'type': 'icon_set',
                                        'icon_style': '5_ratngs'})


workbook.close()

os.startfile(nomeCaminho)
