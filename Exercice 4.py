L = int(input("Nombre de lignes : "))
C = int(input("Nombre de colonnes : "))
matrice = [[0 for j in range(C)] for i in range(L)]
for i in range(L):
    for j in range(C):
        print(matrice[i][j], end=" ")
    print()