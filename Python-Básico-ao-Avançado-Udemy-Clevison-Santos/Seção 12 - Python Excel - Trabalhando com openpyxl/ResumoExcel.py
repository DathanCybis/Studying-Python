from openpyxl import load_workbook
import os

nomeCaminho = 'C:\\...\\Resumo.xlsx'
planilha_aberta = load_workbook(filename=nomeCaminho)

sheet_selecionada = planilha_aberta['Vendas']



planilha_aberta.save(filename=nomeCaminho)

os.startfile(nomeCaminho)
