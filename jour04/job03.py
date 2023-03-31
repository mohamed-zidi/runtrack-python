def initialiser_plateau(n):
    """Crée un plateau de jeu de taille n x n rempli de cases vides"""
    plateau = []
    for i in range(n):
        ligne = []
        for j in range(n):
            ligne.append("O")
        plateau.append(ligne)
    return plateau

def afficher_plateau(plateau):
    """Affiche le plateau de jeu dans le terminal"""
    for ligne in plateau:
        print(" ".join(ligne))

def est_valide(plateau, x, y):
    """Vérifie si une position (x, y) est valide pour placer une dame"""
    n = len(plateau)
    # Vérifie s'il y a une dame sur la même colonne
    for i in range(n):
        if plateau[i][y] == "X":
            return False
    # Vérifie s'il y a une dame sur la même ligne
    for j in range(n):
        if plateau[x][j] == "X":
            return False
    # Vérifie s'il y a une dame sur la diagonale descendante
    i, j = x, y
    while i >= 0 and j >= 0:
        if plateau[i][j] == "X":
            return False
        i -= 1
        j -= 1
    i, j = x, y
    while i < n and j < n:
        if plateau[i][j] == "X":
            return False
        i += 1
        j += 1
    # Vérifie s'il y a une dame sur la diagonale ascendante
    i, j = x, y
    while i >= 0 and j < n:
        if plateau[i][j] == "X":
            return False
        i -= 1
        j += 1
    i, j = x, y
    while i < n and j >= 0:
        if plateau[i][j] == "X":
            return False
        i += 1
        j -= 1
    # Si aucune dame ne peut "prendre" la position (x, y), la position est valide
    return True

def placer_dames(plateau, n, x=0):
    """Place les dames sur le plateau de jeu"""
    if x == n:
        # Toutes les dames ont été placées avec succès
        return True
    for y in range(n):
        if est_valide(plateau, x, y):
            # La position (x, y) est valide pour placer une dame
            plateau[x][y] = "X"
            if placer_dames(plateau, n, x+1):
                # Toutes les dames ont été placées avec succès
                return True
            # Si placer une dame à la position (x, y) ne mène pas à une solution,
            # on remet la case correspondante à vide
            plateau[x][y] = "O"
    # Si toutes les positions ont été testées et aucune solution n'a été trouvée,
    # on retourne False
    return False

# Demande à l'utilisateur de saisir la taille du plateau de jeu
n = int(input("Entrez la taille du plateau de jeu : "))

# # Initialise le plateau de jeu avec des cases vides
initialiser_plateau(n)