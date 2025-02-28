# Alek Hanachian 6226989    

from stringprep import c22_specials
from Chercheur import * 
from Adresse import *
from Bureau import *
from Laboratoire import *

a1 = Adresse("New York", "Manhattan", "10001")
c1 = Chercheur("Dr. Smith", "Professeur", "PC001")
b1 = Bureau("B001", "Machine Learning")
b1.ajouterChercheurs(c1)
l1 = Laboratoire("NY Tech Lab", "Intelligence Artificielle", a1)
l1.ajouterBureau(b1)

#l1.afficherLaboratoire()
    

c2 = Chercheur("Dr. Allaire", "Recherchiste", "PC002")
c3 = Chercheur("Dr. Beaudry", "Ressources Humaines", "PC003")
c4 = Chercheur("Dr. Calvin", "Développement", "PC004")
c5 = Chercheur("Dr. Dubois", "Réseaux", "PC005")
c6 = Chercheur("Dr. Benoit", "Cybersécurité", "PC006")
print(b1.getListeChercheurs())
b1.ajouterChercheurs(c2)
print(b1.getListeChercheurs())
b1.ajouterChercheurs(c3)
print(b1.getListeChercheurs())
b1.ajouterChercheurs(c4)
print(b1.getListeChercheurs())
b1.ajouterChercheurs(c5)
print(b1.getListeChercheurs())
b1.ajouterChercheurs(c6)
print(b1.getListeChercheurs())
    