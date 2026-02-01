from openpyxl import load_workbook
import os

nomeCaminho = 'C:\\...\\FórmulasExcel.xlsx'
planilha_aberta = load_workbook(filename=nomeCaminho)

sheet_selecionada = planilha_aberta['Fór']

sheet_selecionada["A6"] = "SUM(A2:A5)"
sheet_selecionada["B6"] = "SUM(B2:B5)"
sheet_selecionada["D2"] = "=A2+B2"
sheet_selecionada["D3"] = "=A3-B3"
sheet_selecionada["D4"] = "=A3*B3"
sheet_selecionada["D5"] = "=A3/B3"

sheet_selecionada["B12"] = "=MID(A12,1,3)"
sheet_selecionada["C12"] = "=MID(A12,5,3)"
sheet_selecionada["D12"] = "=MID(A12,9,3)"
sheet_selecionada["E12"] = "=MID(A12,13,2)"

planilha_aberta.save(filename=nomeCaminho)

os.startfile(nomeCaminho)
