nbre = None
try:
    nbre = int(input("Entrer un nombre"))
except Exception:
    #raise ValueError("Vous devez entrez un nombre")
    print("Vous devez entrer un nombre !")

print(nbre)