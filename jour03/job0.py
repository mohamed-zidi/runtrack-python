# Demande à l'utilisateur de saisir une chaîne de caractères
chaine = input("Entrez une chaîne de caractères : ")

# Ouvre le fichier "output.txt" en mode écriture
with open("output.txt", "w") as fichier:
    # Écrit la chaîne de caractères dans le fichier
    fichier.write(chaine)

# Affiche un message pour indiquer que l'écriture a été effectuée avec succès
print("La chaîne de caractères a été écrite dans le fichier 'output.txt'.")