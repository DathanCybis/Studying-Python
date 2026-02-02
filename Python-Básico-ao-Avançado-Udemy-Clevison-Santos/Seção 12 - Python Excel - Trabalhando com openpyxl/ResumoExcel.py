from openpyxl import load_workbook
import os

nomeCaminho = 'C:\\...\\Resumo.xlsx'
planilha_aberta = load_workbook(filename=nomeCaminho)

sheet_selecionada = planilha_aberta['Vendas']

somarAmanda = 0
somarElaine = 0
somarLeonardo = 0
somarNicolas = 0

for linha in range(2, len(sheet_selecionada['A'])+1):
    if sheet_selecionada['A%s' % linha].value == 'Amanda Martins':
        somarAmanda = somarAmanda + sheet_selecionada['C%s' % linha].value
    
    elif sheet_selecionada['B%s' % linha].value == 'Eliane Moreira':
        somarElaine = somarAmanda + sheet_selecionada['C%s' % linha].value

    elif sheet_selecionada['B%s' % linha].value == 'Leonardo Almeida':
        somarLeonardo = somarAmanda + sheet_selecionada['C%s' % linha].value

    elif sheet_selecionada['B%s' % linha].value == 'Nicolas Pereira':
        somarNicolas = somarAmanda + sheet_selecionada['C%s' % linha].value
    

planilha_aberta.save(filename=nomeCaminho)

os.startfile(nomeCaminho)
