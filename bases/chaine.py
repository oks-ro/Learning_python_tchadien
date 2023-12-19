chaine = "Koudjo Simon"
print(chaine[1])
print(chaine[1:8])

liste = [3, 2, 7, 0]
liste[1] = 10
print(liste)


############# ERROR ########### chaine[1] = "A"
n_chaine = chaine[0:1] + "A" + chaine[2:]
print(n_chaine)

phrase = "Aujourd'hui, je suis à Lomé"
n_phrase = phrase[0:13] + "Afi est" + phrase[20:23] + "Paris"
print(n_phrase, end="\r")

phrase_1 = "Il est bon et mignon"
n_phrase_1 = "Elle" + phrase_1[2:10] + "ne" + phrase_1[10:20] + "ne"
print(n_phrase_1)

print(phrase.upper()) # transforme toute la phrase en Majuscule
print(phrase.lower()) # transforme toute la phrase en Minuscule

# userInput = input("Entrer un mot en miniscule: ")
# print(userInput[0].upper() + userInput[1:])
#
# print(userInput.capitalize()) # met le premier caractère en majuscule

chaine = "Ali va à l'école"
print("Appel du find => ", chaine.find("ol")) # Rétourne l'indice de l'élement passé en paramètre s'il existe

email = "esig-1001\n6-2021"

print(chaine.split())
print(email.split("-"))
print(email.splitlines())

phrase = "Ama est belle"
phrase_r = phrase.replace("Ama", "Elle")
print(phrase_r)

print(phrase.count("e"))

liste = ["Ama", "Papa", "Koffi"]
ma_chaine = "-".join(liste) # Permet d transformer une liste de chaines de caractères en chaine de caractère
print(ma_chaine)

