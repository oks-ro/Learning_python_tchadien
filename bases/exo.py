from random import randint # importation de la fonction randint

# nbre_al = randint(1, 5) #génère le nombre aléatoire
# nbre_find = False
#
# while nbre_find == False:
#     nbre_saisi = int(input("Entrer un nombre: "))
#     if nbre_saisi == nbre_al:
#         print("Félicitation ⭐! Vous avez trouvé le nombre.")
#         nbre_find = True
#     else:
#         print("Vous n'avez pas trouver le nombre, veuillez réessayer !")

################# Sans l'utilisation d'une varialbe bool ############
# nbre_al = randint(1, 5) #génère le nombre aléatoire
# nbre_saisi = int(input("Entrer un nombre: "))
# if nbre_saisi == nbre_al:
#     print("Félicitation ⭐! Vous avez trouvé le nombre.")
# else:
#     print("Vous n'avez pas trouver le nombre, veuillez réessayer !")
#
# while nbre_saisi != nbre_al:
#     nbre_saisi = int(input("Entrer un nombre: "))
#     if nbre_saisi == nbre_al:
#         print("Félicitation ⭐! Vous avez trouvé le nombre.")
#     else:
#         print("Vous n'avez pas trouver le nombre, veuillez réessayer !")


##########################################################
# liste = ["Petro", "Ama", "Koffi", "Yawa"]
# for nom in liste:
#     print("Bonjour", nom)
#
# ##########################################################
# lst = []
# liste = [i for i in range(10) if i%2==0]
# print(liste)
#
# ##############################################"
# liste = [12, 5, 6, 4, 15] # Déclaration de la liste
# mini = liste[0]
# for number in liste:
#     if number < mini:
#         mini = number
# print("Max number is: ", mini)
# # print(max(liste))
#
# ###########################################################
# voyelle = ["a", "i", "e", "o", "y", "u"]
# consonne = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]
#
# car_saisi = input("Entrer une lettre: ")

# if car_saisi in voyelle:
#     print("Voyelle")
# elif car_saisi in consonne:
#     print("Cosonne")
# else:
#     print("Ce n'est pas une lettre")

###########################################################
# control = 0
# for i in range(len(voyelle)): # Parcours la liste des voyelles
#     if car_saisi == voyelle[i]:
#         print("voyelle")
#         break
#     else:
#         control = control + 1
# if control == len(voyelle):
#     control = 0
#     for j in range(len(consonne)):
#         if car_saisi == consonne[j]:
#             print("Consonne")
#             break
#         else:
#             control = control + 1
# if control == len(consonne):
#     print("Ce n'est pas une lettre")

liste = [1, 2, 4, 3, 9, 6, 10]
liste_pair = []
for i in range(len(liste)):
    if liste[i] % 2 == 0:
        liste[i] = "Pair"
print(liste)