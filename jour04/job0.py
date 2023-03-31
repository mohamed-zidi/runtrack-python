def factorielle(n):
    """Calcule la factorielle d'un nombre entier en utilisant la récursivité"""
    if n == 0:
        return 1
    else:
        return n * factorielle(n - 1)

# Demande à l'utilisateur de saisir un nombre entier
n = int(input("Entrez un nombre entier : "))

# Calcule la factorielle de ce nombre en utilisant la fonction factorielle
resultat = factorielle(n)

# Affiche le résultat
print("La factorielle de", n, "est", resultat)