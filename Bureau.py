from Chercheur import *

class Bureau():
    def __init__(self, code:str, nom:str):
        self.code = code        
        self.nom = nom
        self.__listeChercheurs = []
        self.maxChercheurs = 5
    # constructeur de la classe Bureau

    def ajouterChercheurs(self, nouveauChercheur:Chercheur):
        if len(self.__listeChercheurs) < self.maxChercheurs:
            self.__listeChercheurs.append(nouveauChercheur)
        else:
            print("Erreur, ce bureau contient deja le nombre maximum de chercheurs.")
    # fonction ajouterChercheurs vérifie si la liste __listeChercheurs est pleine, si oui un message d'erreur apparait. Si non, on ajoute le chercheur voulu.

    def getListeChercheurs(self):
        return self.__listeChercheurs
    # getter pour la liste de chercheurs du bureau

    def afficherBureau(self):
        print(f"Bureau {self.nom} ({self.code})")
        for c in self.__listeChercheurs:
            print(c)
    # methode qui imprime les informations du bureau et la liste des chercheurs appartenant a ce bureau
