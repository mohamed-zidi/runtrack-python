# Demande à l'utilisateur de renseigner un nombre entier
taille = int(input("Entrez la taille des mots à chercher : "))

# Initialise le compteur de mots
compteur = 0

# Ouvre le fichier "data.txt" en mode lecture
with open("data.txt", "r") as fichier:
    # Lit le contenu du fichier ligne par ligne
    for ligne in fichier:
        # Sépare chaque mot de la ligne
        mots = ligne.split()

        # Compte le nombre de mots de la taille renseignée
        for mot in mots:
            if len(mot) == taille:
                compteur += 1

# Affiche le nombre de mots de la taille renseignée dans le fichier
print(f"Il y a {compteur} mots de taille {taille} dans le fichier.")