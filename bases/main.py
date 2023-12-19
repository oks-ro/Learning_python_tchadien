# ############ Les variables et opérateurs ###########
# var1 = 7
# var2 = 2
#
# # Somme de var1 et var2
# var3 = var1 + var2
# # Différence entre var1 et var2
# var4 = var1 - var2
# # Multipication de var1 par var2
# var5 = var1 * var2
# #Division de var1 par var2
# var6 = var1 // var2
# # Reste de la division de var1 par var2
# var7 = var1 % var2
#
# print("Var3 = ", var3)
# print("Var4 = ", var4)
# print("Var5 = ", var5)
# print("Var6 = ", var6)
# print("Var7 = ", var7)
#
# nom = "AMA"
# prenom = "Afi"
# email = "ama@gmail.com"
#
# print('Mon nom est: ', nom)
# print('Mon prenom est: ', prenom)
#
# #nom_prenom = nom + " " + prenom
# print("Nom et Prenom: ", nom + " " + prenom)
# print("Email: ", email)
#
# nombre = 409374349347
# print(nombre%10)
# print(nombre%100)
#
# age = input("Entrer votre âge: ")
# age = int(age)
# #age = str(age)
# print("Vous avez", age, "ans")
#
# print(age+9)

############# Les conditions ###########

# age = int(input("Entrer votre âge: "))
#
# if age == 5:
#     print("Vous avez 5 ans")
#     print("ldfdfldjfldjfd")
#     a = 7
#     b = 9
#     print("La somme ", a + b)
# elif age == 7:
#     print("Votre age est égale à 7")
# elif age == 10:
#     print("Votre age est égale à 10")
# else:
#     print("Votre age n'est pas égale ni à 5, ni à 7, ni à 10")
#
#
# print("Je vais terminer")


"""
Exercice : Ecrire yun programme qui prend l'age de l'utlisateur et l'affiche :
- "Vous êtes Minieur" : si son age est inférieur à 14
- "Vous êtes Adolescent" : si son age est compris entre 14 et 17 inclus
- "Vous êtes Majeur" : si son age est supéreur ou égale à 18.
"""

# age = int(input("Entrer votre âge >"))
# if age < 14:
#     print("Vous êtes Minieur")
# elif age <= 17:
#     print("Vous êtes Adolescent")
# else:
#     print("Vous êtes Majeur")

####################### Les boucles ######################
# La boucle for
#for i in range(5, 100+1):
#    print(i)
#########################
"""
Ecrire une programme permettant d'afficher les nombre paire compris entre 1 et 1000.
"""
#for i in range(2, 1000, 2):
#    print(i)

"""
Ecrire un programme qui demande à l'utilisateur d'entrer un nombre. 
Le programme affiche la table de multiplication du nombre que l'utilisateur à entré.
"""
# nbre = int(input("Entrer un nobre : "))
# for i in range(12+1):
#     print(nbre, "*", i, "=", nbre*i)

################## While ##############
#
# i = 0
# while i <= 5:
#     print(i)
#     i = i + 2
#
# for j in range(2, 10, 2):
#     print(j)

# for i in range(1, 5+1):
#     for j in range(i):
#         print("*", end="  ")
#     print()

########### Les listes ##########
liste = ["Ama", 3, 4.5, "nom", "prenom"]
#print(liste[1])

#for elt in liste:
#    print(elt)

# for i in range(len(liste)):
#     print(liste[i])

liste2 = [
    [1, 2, 3],
    [4, 5],
    [7, 8, 9]
]

taille = len(liste2)

for i in range(taille):
    taille_ = len(liste2[i])
    for j in range(taille_):
        print("liste[", i, "][", j ,"] =", liste2[i][j])
    print()


liste2.append([3, 9, 0])
print(liste2)

"""
Programme permettant de faire l'addition de 2 matrices carrées
"""

dimension = int(input("Entrer la longueur $> "))

mat1 = []
mat2 = []

print("-"*20, "Remplissons la première matrice", "-"*20)
for i in range(dimension):
    tmpList = [] # Varaible temporaire permettant de stocker une liste
    for j in range(dimension):
        nbreSaisi = int(input("liste[" + str(i) + "][" + str(j) +"] = "))
        tmpList.append(nbreSaisi)
    mat1.append(tmpList)

print("-"*20, "Remplissons la deuxième matrice", "-"*20)
for i in range(dimension):
    tmpList = []
    for j in range(dimension):
        nbreSaisi = int(input("liste[" + str(i) + "][" + str(j) +"] = "))
        tmpList.append(nbreSaisi)
    mat2.append(tmpList)
print("-"*20, "Affichage des matrices", "-"*20)
print("Matrice 1: ",mat1)
print("Matrice 2: ", mat2)

print("-"*10, "Adition des matrices ...")

mat_som = []
for t in range(dimension):
    mat_som.append([])

for i in range(dimension):
    for j in range(dimension):
        mat_som[i].append(mat1[i][j] + mat2[i][j])

print(mat_som)
