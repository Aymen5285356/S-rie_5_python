notes = []
for i in range(8):
    notes_etudiant = []
    for j in range(3):
        note = float(input(f"Note stagiaire {i+1}, module {j+1} : "))
        notes_etudiant.append(note)
    notes.append(notes_etudiant)

def moyenne_generale(notes):
    somme = 0
    total_notes = 0
    for etudiant in notes:
        for note in etudiant:
            somme += note
            total_notes += 1
    return somme / total_notes

def note_maximale(notes):
    max_note = notes[0][0]
    for etudiant in notes:
        for note in etudiant:
            if note > max_note:
                max_note = note
    return max_note

def reussite(notes):
    indices = []
    for i in range(len(notes)):
        moyenne_etudiant = sum(notes[i]) / len(notes[i])
        if moyenne_etudiant >= 10:
            indices.append(i)
    return indices

print(moyenne_generale(notes))
print(note_maximale(notes))
print(reussite(notes))