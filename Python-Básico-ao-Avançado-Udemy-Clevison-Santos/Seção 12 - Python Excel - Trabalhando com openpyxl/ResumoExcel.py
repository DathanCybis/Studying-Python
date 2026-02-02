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

sheet_resumo = planilha_aberta.create.sheet(title="Resumo")

sheet_resumo = ['A1'] = 'Vendedores'   
sheet_resumo = ['B1'] = 'Vendas'   

sheet_resumo = ['A2'] = 'Amanda Martins'   
sheet_resumo = ['B2'] = somarAmanda

sheet_resumo = ['A3'] = 'Eliane Moreira'
sheet_resumo = ['B3'] = somarElaine

sheet_resumo = ['A4'] = 'Leonardo Almeida' 
sheet_resumo = ['B4'] = somarLeonardo

sheet_resumo = ['A5'] = 'Nicolas Pereira' 
sheet_resumo = ['B5'] = somarNicolas


planilha_aberta.save(filename=nomeCaminho)

os.startfile(nomeCaminho)
