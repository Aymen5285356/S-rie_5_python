tableau = []
for i in range(3):
    ligne = []
    for j in range(2):
        valeur = int(input(f"Entier pour ligne {i+1}, colonne {j+1} : "))
        ligne.append(valeur)
    tableau.append(ligne)
print(tableau)