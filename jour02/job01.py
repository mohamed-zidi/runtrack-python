class Personne:
    def __init__(self, nom, prenom):
        self.__nom = nom
        self.__prenom = prenom
    
    def SePresenter(self):
        print(f"Je m'appelle {self.__prenom} {self.__nom}")
    
    def getNom(self):
        return self.__nom
    
    def setNom(self, nouveau_nom):
        self.__nom = nouveau_nom
    
    def getPrenom(self):
        return self.__prenom
    
    def setPrenom(self, nouveau_prenom):
        self.__prenom = nouveau_prenom


class Auteur(Personne):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.__oeuvre = []
    
    def listerOeuvre(self):
        print(f"Oeuvre de {self.getPrenom()} {self.getNom()}:")
        for livre in self.__oeuvre:
            print(livre.getTitre())
    
    def ecrireUnLivre(self, titre):
        livre = Livre(titre, self)
        self.__oeuvre.append(livre)
    
    def getOeuvre(self):
        return self.__oeuvre


class Livre:
    def __init__(self, titre, auteur):
        self.__titre = titre
        self.__auteur = auteur
    
    def print(self):
        print(self.__titre)
    
    def getTitre(self):
        return self.__titre
    
    def getAuteur(self):
        return self.__auteur
    

# Création d'un auteur
auteur1 = Auteur("Hugo", "Victor")

# Création de deux livres pour cet auteur
auteur1.ecrireUnLivre("Les Misérables")
auteur1.ecrireUnLivre("Notre-Dame de Paris")

# Affichage de la liste des livres écrits par l'auteur
auteur1.listerOeuvre()  # Affiche "Oeuvre de Victor Hugo:\nLes Misérables\nNotre-Dame de Paris"