from openpyxl import load_workbook
import os

nomeArquivo = "C:\\...\\...\\Quebrar.xlsx"

planilha_aberta = load_workbook(filename=nomeArquivo)

sheet_selecionada = planilha_aberta['Dados']

nomeNovo = ""
totalLinha = len(sheet_selecionada['A']) + 1

for linha in range(2, totalLinha):
    nomeAtual = sheet_selecionada['A%s' % linha].value

    if nomeNovo == nomeAtual:
        pass
    else:
