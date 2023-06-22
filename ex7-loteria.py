file_path = 'loteria.txt'
with open(file_path, 'r') as file:
    matrix_data = file.readlines()
matrix = [line.split() for line in matrix_data]

acumula_multiplos_linha = 0
qtd_col1 = 0
qtd_col2 = 0
qtd_col3 = 0
total_duplo_triplo = 0

for row in matrix:
    for i in range(len(row)):
        if (i == 0 and int(row[i]) == 1):
            qtd_col1 = qtd_col1 + 1
        elif(i == 1 and int(row[i]) == 1):
            qtd_col2 = qtd_col2 + 1
        elif(i == 2 and int(row[i]) == 1):
            qtd_col3 = qtd_col3 + 1
        if (int(row[i]) == 1):
            acumula_multiplos_linha = acumula_multiplos_linha + 1
        i = i + 1
    if(acumula_multiplos_linha == 2):
        print("DUPLO")
        total_duplo_triplo = total_duplo_triplo + 1
    elif(acumula_multiplos_linha == 3):
        print("TRIPLO")    
        total_duplo_triplo = total_duplo_triplo + 1
    acumula_multiplos_linha = 0
print("qtd de marcacoes na coluna 1: ",qtd_col1)
print("qtd de marcacoes na coluna 2: ",qtd_col2)
print("qtd de marcacoes na coluna 3: ",qtd_col3)
print("total duplos e triplos: ",total_duplo_triplo)
