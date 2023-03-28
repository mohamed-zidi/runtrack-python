class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom


class Client(Personne):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.collection = []

    def inventaire(self):
        print(f"Collection de livres de {self.nom} {self.prenom} :")
        for livre in self.collection:
            print(livre.titre)

class Bibliotheque:
    def __init__(self, nom):
        self.nom = nom
        self.catalogue = {}

    def acheterLivre(self, auteur, titre, quantite):
        for livre in auteur.oeuvre:
            if livre.titre == titre:
                if titre in self.catalogue:
                    self.catalogue[titre] += quantite
                else:
                    self.catalogue[titre] = quantite
                print(f"Le livre '{titre}' a été ajouté au catalogue avec une quantité de {quantite}.")
                return
        print(f"Le livre '{titre}' n'existe pas dans l'oeuvre de {auteur.nom} {auteur.prenom}.")

    def inventaire(self):
        print(f"Catalogue de la bibliothèque {self.nom} :")
        for titre, quantite in self.catalogue.items():
            print(f"'{titre}' - quantité : {quantite}")

    def louer(self, client, titre):
        if titre in self.catalogue and self.catalogue[titre] > 0:
            self.catalogue[titre] -= 1
            client.collection.append(titre)
            print(f"Le livre '{titre}' a été loué par {client.nom} {client.prenom}.")
        else:
            print(f"Le livre '{titre}' n'est pas disponible.")

    def rendreLivres(self, client):
        for titre in client.collection:
            if titre in self.catalogue:
                self.catalogue[titre] += 1
            else:
                self.catalogue[titre] = 1
        client.collection = []


class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur


class Auteur(Personne):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.oeuvre = []

    def ecrireLivre(self, titre):
        livre = Livre(titre, self)
        self.oeuvre.append(livre)
        print(f"{self.nom} {self.prenom} a écrit le livre '{titre}'.")

# Exemple d'utilisation :

# Instanciation d'auteurs et création de livres
auteur1 = Auteur("Hugo", "Victor")
auteur1.ecrireLivre("Les Misérables")
auteur2 = Auteur("Zola", "Emile")
auteur2.ecrireLivre("Germinal")
auteur2.ecrireLivre("Nana")

# Création d'une bibliothèque et achat de livres
bibliotheque = Bibliotheque("Bibliothèque municipale")
bibliotheque.acheterLivre(auteur1, "Les Misérables", 5)
bibliotheque.acheterLivre(auteur2, "Germinal", 3)
bibliotheque.acheterLivre(auteur2, "Nana", 2)
bibliotheque.inventaire()