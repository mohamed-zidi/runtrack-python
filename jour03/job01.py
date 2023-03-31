# Ouvre le fichier "output.txt" en mode lecture
with open("output.txt", "r") as fichier:
    # Lit le contenu du fichier
    contenu = fichier.read()

# Affiche le contenu du fichier dans le terminal
print(contenu)