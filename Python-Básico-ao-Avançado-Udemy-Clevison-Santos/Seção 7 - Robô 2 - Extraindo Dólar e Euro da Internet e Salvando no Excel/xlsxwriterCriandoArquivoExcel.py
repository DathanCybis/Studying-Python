import os
import xlsxwriter

# Caminho onde o arquivo será salvo (pasta atual)
caminho = os.path.join(os.getcwd(), "dados.xlsx")

# Cria o arquivo Excel
workbook = xlsxwriter.Workbook(caminho)

# Cria uma planilha
worksheet = workbook.add_worksheet("Planilha1")

# Escrevendo os dados
worksheet.write("A1", "Nome")
worksheet.write("B1", "João")

worksheet.write("A2", "Idade")
worksheet.write("B2", 25)

# Fecha o arquivo (muito importante)
workbook.close()

print("Planilha criada com sucesso!")

os.startfile(caminho)
