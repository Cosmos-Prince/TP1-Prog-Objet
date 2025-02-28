# Alek Hanachian 6226989    
from stringprep import c22_specials
from Chercheur import * 
from Adresse import *
from Bureau import *
from Laboratoire import *

def separation():
    print('\n','*' * 40, '\n')
# pour meilleure lisibilité dans la console en séparant les sections d'affichage


########## MISE EN OEUVRE & RÉSULTAT FINAL ##########
# 1. Création & manipulation des instances 
a1 = Adresse("New York", "Manhattan", "10001")
c1 = Chercheur("Dr. Smith", "Professeur", "PC001")
b1 = Bureau("B001", "Machine Learning")
b1.ajouterChercheurs(c1)
l1 = Laboratoire("NY Tech Lab", "Intelligence Artificielle", a1)
l1.ajouterBureau(b1)

# 2. Preuve que afficherLaboratoire() fonctionne 
l1.afficherLaboratoire()
    
separation()

########## TESTS DES DIFFÉRENTS GETTER, SETTERS, ET VALEURS MAXIMALES ##########

# Tests pour la classe Adresse

print(f"Adresse de a1: {a1.getCodePostal()}")
a1.setCodePostal("202020")
print(f"Nouvelle adresse de a1: {a1.getCodePostal()}")
print(f"Preuve de la méthode __str__ de la classe Adresse: {a1.__str__()}")

separation()

# Tests pour la classe Chercheur

print(f"Getter du numéro d'ordinateur: {c1.getNumeroOrdi()}")
c1.setNumeroOrdi("PC111")
print(f"Nouveau numéro d'ordinateur: {c1.getNumeroOrdi()}")
print(f"Preuve de la méthode __str__ de la classe Chercheur: {c1.__str__()}")

separation()

# Tests pour la classe Professeur, enfant de Chercheur

p1 = Professeur("M. Ivanof", "Professeur en recherche", "PC900", "Recherche")
print(f"Getter de la spécialité du professeur: {p1.getSpecialite()}")
p1.setSpecialite("Développement")
print(f"Nouvelle Valeur de la spécialité du professeur: {p1.getSpecialite()}")

separation()

# Test pour la classe Bureau

c2 = Chercheur("Dr. Allaire", "Recherchiste", "PC002")
c3 = Chercheur("Dr. Beaudry", "Ressources Humaines", "PC003")
c4 = Chercheur("Dr. Calvin", "Développement", "PC004")
c5 = Chercheur("Dr. Dubois", "Réseaux", "PC005")
c6 = Chercheur("Dr. Benoit", "Cybersécurité", "PC006")
# création de 6 chercheurs totaux pour s'assurer qu'il y a un message d'erreur pour ajouter le 6e

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
print("Affiche l'erreur et montre qu'il reste les 5 mêmes chercheurs qu'avant l'essai d'ajouter un 6e")
# Ajout d'un chercheur à la fois + affichage de la liste à chaque nouvelle addition

print("Preuve de la fonctionnalité de la méthode afficherBureau: ")
b1.afficherBureau()

separation()

# Tests pour la classe Laboratoire

listeBureaux:list = []

for i in range(2, 52):
    if i >= 10:
        listeBureaux.append(Bureau(f"B0{i}",f"Bureau {i}"))
    else:
        listeBureaux.append(Bureau(f"B00{i}",f"Bureau {i}"))
    # séparation des valeurs de i pour un plus bel affichage, gardant toujours 3 digits

#print(listeBureaux)
for b in listeBureaux:
    l1.ajouterBureau(b)
    print(l1.getBureaux(), "\n")
# ajoute un bureau à la fois et affiche la nouvelle liste de bureaux étant reliés au Labo 1
# démontre aussi la fonctionnalité de getBureaux

# afficherLaboratoire à déjà été démontré au début du fichier
