from Bureau import *
from Adresse import *

class Laboratoire():
    def __init__(self, nom:str, specialite:str, adresse:Adresse):
        self.nom = nom
        self.specialite = specialite
        self.adresse = adresse
        self.__bureau = []
        self.maxBureaux = 50
    # constructeur de la classe laboratoire

    def ajouterBureau(self, bureau:Bureau):
        if len(self.__bureau) < self.maxBureaux:
            self.__bureau.append(bureau)
        else:
            print("Erreur, ce Laboratoire est deja plein.")
    # méthode pour ajouter des bureaux dans le labo s'il reste de la place, 
    # en comparant la longeueur de la liste __bureau a la quantite maximale de bureaux possibles

    def getBureaux(self):
        return self.__bureau
    # getter pour la liste des bureaux du labo

    def afficherLaboratoire(self):
        print(f"{self.nom} - {self.specialite}")
        print(f"Adresse: {self.adresse}")
        for b in self.__bureau:
            b.afficherBureau()
    # methode pour afficher toutes les informations du laboratoire
    