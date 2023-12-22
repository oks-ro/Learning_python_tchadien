f = open("mon_fichier", "a")
f.write("Ma première ligne\n")
f.write("Ma deuxième ligne\n")
f.close()

with open("mon_fichier", "a") as f:
    f.write("Ama")
    f.write("4")

f_read = open("mon_fichier", "r")
mes_donnees = f_read.readline()
f_read.close()
print(mes_donnees)




#########################################################

with open("mdp.txt", "w") as f_mdp:
    f_mdp.write("ama\n")
    f_mdp.write("koffi\n")
    f_mdp.write("pipi\n")
    f_mdp.write("kossi\n")
    f_mdp.write("afi\n")
    f_mdp.write("toto\n")
    f_mdp.write("1235\n")



with open("mdp.txt", "r") as f:
    userInput = input("Entrer votre mot de passe: ")
    while True:
        pwd_line = f.readline()
        print("PWD line = ", type(pwd_line))
        if userInput+"\n" == pwd_line:
            print("J'ai trouver le mot de passe")
            break
        if pwd_line == '':
            break