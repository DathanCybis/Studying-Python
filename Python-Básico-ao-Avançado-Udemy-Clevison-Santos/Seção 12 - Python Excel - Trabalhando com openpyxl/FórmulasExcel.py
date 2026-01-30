from openpyxl import load_workbook
import os

nomeCaminho = 'C:\\...\\Fórmulas.xlsx'
planilha_aberta = load_workbook(filename=nomeCaminho)

sheet_selecionada = planilha_aberta['Professor']

sheet_selecionada["A6"] = "SUM(A2:A5)"
sheet_selecionada["B6"] = "SUM(B2:B5)"

planilha_aberta.save(filename=nomeCaminho)

os.startfile(nomeCaminho)
