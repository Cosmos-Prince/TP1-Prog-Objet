class Chercheur:
    def __init__(self, nom:str, poste:str, numOrdi:str):
        self.nom = nom
        self.poste = poste
        self.__numeroOrdi = numOrdi
        self.__appartientABureau:list = []
        self.__maxBureau:int = 5
    # constructeur de la classe Chercheur

    def getNumeroOrdi(self):
        return self.__numeroOrdi
    # getter pour le num�ro d'ordi

    def setNumeroOrdi(self, nouveauNum:str):
        self.__numeroOrdi = nouveauNum
    # setter pour le numéro d'ordi

    def getListeBureau(self):
        return self.__appartientABureau
    # getter pour la liste de bureaux auquel le chercheur appartient

    def addListeBureau(self, valeur):
        self.__appartientABureau.append(valeur)
    # ajoute une valeur de plus à la liste de bureaux auquel le chercheur appartient

    def getMaxBureaux(self):
        return self.__maxBureau
    # getter pour le maximum de bureaux auquel un chercheur peut appartenir

    def __str__(self):
        return f"Chercheur: {self.nom}, {self.poste}, {self.__numeroOrdi}"
    # methode __str__ qui retourne les informations de la classe Chercheur

    def __repr__(self):
        return f"{self.__str__()} \n"
    # méthode __repr__ pour afficher les informations de la classe chercheur dans les getters
    # des autres classes utilisant ces informations puisque print(self.__listeChercheurs)
    # utilise __repr__ et non __str__





class Professeur(Chercheur):
    def __init__(self, nom:str, poste:str, numOrdi:str, specialite:str):
        super().__init__(nom, poste, numOrdi)
        self.__specialite = specialite
    # constructeur de la classe Professeur avec heritage de la classe Chercheur

    def getSpecialite(self):
        return self.__specialite
    # getter pour la spécialité

    def setSpecialite(self, valeur:str):
        self.__specialite = valeur
    # setter pour la spécialité

