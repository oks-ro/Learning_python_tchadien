from random import randint

nbre_essai = 0


def gererNiveau():
    repeat = True
    nbreChance = None
    while repeat:
        print("################ CHOX DU NIVEAU ################")
        print("1. Facile")
        print("2. Moyen")
        print("3. Difficile")
        choix = int(input("Veuillez entre votre choix $> "))
        if choix == 1:
            nbreChance = 15
            repeat = False
        elif choix == 2:
            nbreChance = 10
            repeat = False
        elif choix == 3:
            nbreChance = 5
            repeat = False
        else:
            print("CHOIX EST INVALID !\n")
    return nbreChance


def afficherNbreEssaiRestant(nbre_essai_restant):
    print(f"Il vous reste {nbre_essai_restant} essai(s)")


def guiderUtilisateur(nbre_al, nbre_saisi, nbre_essai):
    if nbre_saisi > nbre_al:
        print("Le nbre saisi est plus grand")
        print("Il vous reste", nbre_essai, "essai(s)")
    elif nbre_saisi < nbre_al:
        print("Le nbre saisi est plus petit")
        print("Il vous reste", nbre_essai, "essai(s)")
    else:
        print("Félicitation ⭐⭐⭐, Vous avez trouvez.")
        return "FIND"


def genererLenombreAl():
    nber_gen = randint(1, 100)
    return nber_gen


def jouer():
    nbre_essai = gererNiveau()
    print("*********", nbre_essai)
    nbre_al = genererLenombreAl()
    print("Le nbre Al: ", nbre_al)
    while nbre_essai > 0:
        nbre_saisi = None
        try:
            nbre_saisi = int(input("Deviner le nombre $$$$> "))
        except Exception:
            return "Valeur invalid !"
        nbre_essai = nbre_essai - 1
        return_value = guiderUtilisateur(nbre_al, nbre_saisi, nbre_essai)
        if return_value == "FIND":
            return
