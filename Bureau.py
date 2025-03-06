from Chercheur import *

class Bureau():
    def __init__(self, code:str, nom:str):
        self.code = code        
        self.nom = nom
        self.__listeChercheurs = []
        self.maxChercheurs = 5
    # constructeur de la classe Bureau

    def __repr__(self):
        return f"Bureau: {self.nom} ({self.code})"
    # permets au listes d'afficher le résultat souhaité (les informations du bureau)

    def ajouterChercheurs(self, nouveauChercheur:Chercheur):
        if len(self.__listeChercheurs) < self.maxChercheurs:
            if nouveauChercheur.getMaxBureaux() > len(nouveauChercheur.getListeBureau()):
                nouveauChercheur.addListeBureau(self)
                self.__listeChercheurs.append(nouveauChercheur)
            # 2e check pour vérifier si le chercheur est déjà dans un maximum de bureaux possibles 
            # (demandé par le professeur à l'oral le 6/03 après une question par rapport à la formulation de l'énoncé du TP)
            else:
                print(f"Erreur, le chercheur {nouveauChercheur} est déja dans {nouveauChercheur.getMaxBureaux()} bureaux et ne peux plus être ajouté dans d'autres.")
        else:
            print("Erreur, ce bureau contient deja le nombre maximum de chercheurs.")
    # fonction ajouterChercheurs vérifie si la liste __listeChercheurs est pleine, 
    # si oui un message d'erreur apparait. Si non, on ajoute le chercheur voulu.

    def getListeChercheurs(self):
        return self.__listeChercheurs
    # getter pour la liste de chercheurs du bureau

    def afficherBureau(self):
        print(f"Bureau {self.nom} ({self.code})")
        for c in self.__listeChercheurs:
            print(c)
    # methode qui imprime les informations du bureau et la liste des chercheurs appartenant a ce bureau
