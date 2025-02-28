class Adresse:
    def __init__(self, etat:str, ville:str, codePostal:str):
        self.etat = etat
        self.ville = ville
        self.__codePostal = codePostal
    # constructeur de la classe Adresse

    def getCodePostal(self):
        return self.__codePostal
    # getter pour le code postal
    
    def setCodePostal(self, nouvelleValeur:str):
        self.__codePostal = nouvelleValeur
    # setter pour le code postal

    def __str__(self):
        return f"{self.ville}, {self.etat} - {self.__codePostal}"
    # methode __str__ qui retourne les informations de la classe
