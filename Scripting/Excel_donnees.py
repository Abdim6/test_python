"Extraire des données depuis un fichier excel : "

import openpyxl

wb = openpyxl.load_workbook("novembre.xlsx", data_only=True)
print(wb.sheetnames)

"Feuille = sheet"
"Quand tu veux une feuille spécifique du fichier excel"
# sheet = wb["Feuil1"]
"Quand tu veux juste accéder à la feuil active"
sheet = wb.active
sheet.max_column
for row in range(2,sheet.max_row+1):
    for column in range(1,sheet.max_column+1):
    # cell1 = sheet.cell(3,3)
        print(sheet.cell(row,column).value)
    print("-----")