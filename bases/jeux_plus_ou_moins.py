from random import randint

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

def genererLenombreAl():
    nber_gen = randint(1, 100)
    return nber_gen

def jouer():
    gererNiveau()
    nbre_al = genererLenombreAl()
    print("Le nbre Al: ", nbre_al)
    while nbre_essai > 0:
        nbre_saisi = int(input("Deviner le nombre $$$$> "))
        if nbre_saisi > nbre_al:
            print("Le nbre saisi est plus grand")
            nbre_essai = nbre_essai - 1
            print("Il vous reste", nbre_essai, "essai(s)")
        elif nbre_saisi < nbre_al:
            print("Le nbre saisi est plus petit")
            nbre_essai = nbre_essai - 1
            print("Il vous reste", nbre_essai, "essai(s)")
        else:
            print("Félicitation ⭐⭐⭐, Vous avez trouvez.")
            return

if __name__=="__main__":
    jouer()
