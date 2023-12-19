"""
Pour déclarer une fonction, on utilise le mot clé
`def` suivi du nom de la fonction
"""


def reste_division(nbre1, nbre2=6):
    return nbre1 % nbre2


# print(reste_division(nbre1=24, nbre2=7))


def dire_bonjour(nom):
    return "Bonjour " + nom


#print(dire_bonjour("Rebecca"))

"""
Ecrivez une fonction qui prend en parametre une liste.
Et retourne la valeur maximale de cette liste.
"""

def minimal(liste):
    min = liste[0]
    for elt in liste:
        if elt < min:
            min = elt
    return min

print(minimal([3, 7, 2, 4]))


def liste_pair(liste):
    """
    Cette fonction permet à l'utilisateur de trouver la liste des nombres
    pairs à partir d'une liste transmise en paramètre
    :param liste: est une liste d'entrée
    :return: une liste contenant seulement les nombre pairs
    """
    nbre_pair_list = []
    for elt in liste:
        if elt % 2 == 0:
            nbre_pair_list.append(elt)
    return nbre_pair_list

print(help(liste_pair))


liste = [3, 8, 0, 7, 17, 4]
liste_nbres_pair = [x/2 for x in liste if x % 2 == 0]
print("Les nombres paires: ", liste_nbres_pair)

list_sec = []
for x in liste:
    if x % 2 == 0:
        list_sec.append(x)

print(list_sec)

print(liste)
print([3 * x for x in liste if x % 2 != 0]) # list comprehension

############################################# TRANCHES ######################################
liste = [1, 3, 4, 7, 0, 2, 9, 42]
print(liste[-1])

liste_ = liste[0:3]
print(liste_)

liste__ = liste[0:6:2]
print(liste__)

####################################################
print("****** liste = ", liste)
del liste[1] # Supprime l'élement à l'indice 1 dans la liste
print(liste)

liste.insert(2, 18)
print(liste)

liste.append(30)
print(liste)

listeNbre = []
nbre_saisi = int( input("Entrer un nbre: "))
while nbre_saisi >= 0:
    listeNbre.append(nbre_saisi)
    nbre_saisi = int(input("Entrer un nbre: "))

print(sum(listeNbre))