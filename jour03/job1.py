# Initialise un dictionnaire pour stocker les extensions de domaines et leur nombre d'occurrences
import re


occurrences = {}

# Ouvre le fichier "domains.xml" en mode lecture
with open("domains.xml", "r") as fichier:
    # Lit le contenu du fichier ligne par ligne
    for ligne in fichier:
        # Recherche toutes les extensions de domaines présentes dans la ligne
        extensions = re.findall(r'\.[a-z]+', ligne)

        # Incrémente le nombre d'occurrences de chaque extension de domaines dans le dictionnaire
        for extension in extensions:
            if extension in occurrences:
                occurrences[extension] += 1
            else:
                occurrences[extension] = 1

# Affiche le nombre d'occurrences de chaque extension de domaines dans le fichier
for extension, nombre in occurrences.items():
    print(f"{extension}: {nombre}")