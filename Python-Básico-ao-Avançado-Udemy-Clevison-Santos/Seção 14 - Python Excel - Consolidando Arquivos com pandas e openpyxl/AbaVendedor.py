from openpyxl import load_workbook
import os

nomeArquivo = "C:\\...\\...\\Quebrar.xlsx"

planilha_aberta = load_workbook(filename=nomeArquivo)

sheet_selecionada = planilha_aberta['Dados']

