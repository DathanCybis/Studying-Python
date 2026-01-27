from openpyxl import load_workbook
import os

nomeCaminho = 'C:\\...\\DeletarLinhaColunaExcel.xlsx'
planilha_aberta = load_workbook(filename=nomeCaminho)

sheet_selecionada = planilha_aberta['Professor']

sheet_selecionada.delete_rows(3)
sheet_selecionada.delete_rows(3)
sheet_selecionada.delete_rows(5)

sheet_selecionada.delete_cols(2)

planilha_aberta.save(filename=nomeCaminho)

os.startfile(nomeCaminho)
