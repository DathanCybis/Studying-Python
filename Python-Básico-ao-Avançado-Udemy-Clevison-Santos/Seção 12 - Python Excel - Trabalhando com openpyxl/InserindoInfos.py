from openpyxl import load_workbook
import os

nomeCaminho = 'C:\\...\\InserindoInfos.xlsx'
planilha_aberta = load_workbook(filename=nomeCaminho)

sheet_selecionada = planilha_aberta['Professor']

dadosTabela = [
    ['Nome', 'Idade'],
    ['Berenice', 28],
    ['Caio', 32],
    ['Nicole', 34],
    ['Leonardo', 19],
    ['Amanda', 25]
]





planilha_aberta.save(filename=nomeCaminho)

os.startfile(nomeCaminho)
