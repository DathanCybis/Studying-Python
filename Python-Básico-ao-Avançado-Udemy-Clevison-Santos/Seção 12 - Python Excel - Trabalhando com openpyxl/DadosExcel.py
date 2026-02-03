from openpyxl import load_workbook
from openpyxl import workbook
import os

nomeCaminho = 'C:\\...\\DadosExcel.xlsx'
planilha_aberta = load_workbook(filename=nomeCaminho)

sheet_selecionada = planilha_aberta['Professor']






planilha_aberta.save(filename=nomeCaminho)

os.startfile(nomeCaminho)
