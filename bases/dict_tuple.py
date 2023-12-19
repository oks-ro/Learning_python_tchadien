mon_dict = {}
dict
mon_dict['nom'] = 'Ama'
mon_dict['prenom'] = 'Kwatcha'
mon_dict['age'] = 25

print(mon_dict)
print(mon_dict['nom']) # Affiche la valeur associciée à la clé `nom`

print(mon_dict.keys()) # rétourne une liste contenant les clés du dictionnaire
print(mon_dict.values()) # rétourne une liste contenant les valeurs du dictionnaire

if "nom" in mon_dict:
    print("La clé est présente.")
else:
    print("La clé n'existe pas")

dict_list = [
    {"nom":"Ali", "prenom":"Toto", "Age":15},
    {"nom":"Papavi", "prenom":"Allo", "Age":56},
    {"nom":"Koffi", "prenom":"Komlan", "Age":30},
]

ditio = {"Username":"toto", "learn_course":["Intro à Python", "Base de données SQL", "Les du Resaux", "Les bases de CS"]}

print(dict_list[0]['nom'])

for personne in dict_list:
    print(personne['Age'])

print("************ Affichage des cours suivi ******")
for elt in ditio['learn_course']:
    print("***",elt)

######################################### TUBLE #########################
mon_tuple = (1, 4, 7, 81)

mon_tuple = mon_tuple + (3, )
print(mon_tuple)
print(mon_tuple[0])
print(mon_tuple[1:4])

liste = [2, 8, 9, 0]
print(liste)
liste_tuple = tuple(liste)
print(liste_tuple)