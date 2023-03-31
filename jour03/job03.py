import matplotlib.pyplot as plt
import string

# Initialise un dictionnaire pour stocker le nombre d'occurrences de chaque lettre
occurrences = {char: 0 for char in string.ascii_lowercase}

# Ouvre le fichier "data.txt" en mode lecture
with open("data.txt", "r") as fichier:
    # Lit le contenu du fichier ligne par ligne
    for ligne in fichier:
        # Convertit la ligne en minuscules
        ligne = ligne.lower()

        # Incrémente le nombre d'occurrences de chaque lettre dans le dictionnaire
        for char in ligne:
            if char in occurrences:
                occurrences[char] += 1

# Calcule le nombre total de lettres dans le fichier
total = sum(occurrences.values())

# Calcule le pourcentage d'apparition de chaque lettre et le stocke dans une liste
pourcentages = [occurrences[char] / total * 100 for char in string.ascii_lowercase]

# Affiche l'histogramme représentant le pourcentage d'apparition de chaque lettre
plt.bar(string.ascii_lowercase, pourcentages)
plt.xlabel("Lettre")
plt.ylabel("% d'apparition")
plt.show()