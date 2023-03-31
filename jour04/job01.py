def puissance(x, n):
    """Calcule la puissance d'un nombre x à la n-ième puissance en utilisant la récursivité"""
    if n == 0:
        return 1
    else:
        return x * puissance(x, n - 1)

# Demande à l'utilisateur de saisir un nombre entier et un nombre réel
n = int(input("Entrez un nombre entier pour la puissance : "))
x = float(input("Entrez un nombre réel : "))

# Calcule la puissance de x à la n-ième puissance en utilisant la fonction puissance
resultat = puissance(x, n)

# Affiche le résultat
print(x, "élevé à la puissance", n, "est égal à", resultat)