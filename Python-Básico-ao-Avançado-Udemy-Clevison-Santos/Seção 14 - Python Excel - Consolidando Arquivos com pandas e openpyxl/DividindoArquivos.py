from openpyxl import load_workbook
from openpyxl import Workbook
import os

nomeArquivo = "C:\\...\\...\\DividindoArquivos.xlsx"

planilha_aberta = load_workbook(filename=nomeArquivo)

sheet_selecionada = planilha_aberta['Dados']

criandoNovoExcel = Workbook()

nomeNovo = ""
totalLinha = len(sheet_selecionada['A']) + 1

for linha in range(2, totalLinha):
    nomeAtual = sheet_selecionada['A%s' % linha].value

    if nomeNovo == nomeAtual:
        linhaSheet = len(sheet_selecionada2['A'] + 1)
        celulaColunaA = "A" + str(linhaSheet)
        celulaColunaB = "B" + str(linhaSheet)
        celulaColunaC = "C" + str(linhaSheet)

        sheet_selecionada2[celulaColunaA] = sheet_selecionada['A%s' % linha].value
        sheet_selecionada2[celulaColunaB] = sheet_selecionada['B%s' % linha].value
        sheet_selecionada2[celulaColunaC] = sheet_selecionada['C%s' % linha].value

    else:
        sheet_resumo = planilha_aberta.create_sheet(title=nomeAtual)

        sheet_selecionada2 = planilha_aberta[nomeAtual]

        nomeAtual = sheet_selecionada['A%s' % linha].value

        nova_planilha = criandoNovoExcel.active

        nova_planilha.title = "Vendas"

        caminhoNovaPlanilha = "C:\\...\\...\\DividindoArquivos.xlsx"

        sheet_selecionada2['A1'] = "Vendedor"
        sheet_selecionada2['B1'] = "Produtos"
        sheet_selecionada2['C1'] = "Vendas"

        sheet_selecionada2['A2'] = sheet_selecionada['A%s' % linha].value
        sheet_selecionada2['B2'] = sheet_selecionada['B%s' % linha].value
        sheet_selecionada2['C2'] = sheet_selecionada['C%s' % linha].value

        criandoNovoExcel.save(filename=caminhoNovaPlanilha)

planilha_aberta.save(filename=nomeArquivo)

os.startfile(nomeArquivo)
