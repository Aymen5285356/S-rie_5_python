jours_semaine = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
mois_annee = ["Janvier", "Fevrier", "Mars", "Avril", "Mai", "Juin", "Juillet", "Aout", "Septembre", "Octobre", "Novembre", "Decembre"]
jours_mois = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

jour_semaine = 0
for mois in range(12):
    for jour in range(1, jours_mois[mois] + 1):
        print(f"{jours_semaine[jour_semaine]} {jour} {mois_annee[mois]} 2024")
        jour_semaine = (jour_semaine + 1) % 7