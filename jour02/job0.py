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
    


jean = Personne("De La Fontaine", "Jean")
jean.SePresenter()

jean.setNom("Michel")
jean.SePresenter()

elodie = Personne("Menard", "Elodie")
elodie.SePresenter()