import xlsxwriter 
import os

caminhoArquivo = "C\\...\\..."

planilha = xlsxwriter.workbook(caminhoArquivo)

planilha1 = planilha.add_worksheet()

planilha1.write("A1", "Nome")

planilha.close()

os.startfile(caminhoArquivo)
