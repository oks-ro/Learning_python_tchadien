def find_(chain, searchKey):
    index = None
    for i in range(len(chain)):
        if chain[i] == searchKey:
            index = i
            break
    if index is not None:
        return index
    else:
        return -1


returned = find_("Ama est à la maison", "p")
print(returned)


def find_2(chain, search_key):
    index = None
    for i in range(len(chain)):
        if len(search_key) == 0:
            return -1
        if len(search_key) == 1:
            for i in range(len(chain)):
                if chain[i] == search_key:
                    index = i
                    break
            if index is not None:
                return index
            else:
                return -1
        if chain[i] == search_key[0]:
            count = 0
            for j in range(i, i + len(search_key)):
                if chain[j] == search_key[count]:
                    count = count + 1
                    if count == len(search_key) - 1:
                        index = i
                        break
                else:
                    break
    if index is not None:
        return index
    else:
        return -1


returned_2 = find_2("Ama est à la maison", "est")
print("Find 2: ", returned_2)


def split_(chaine, p=" "):
    liste = []
    space_indice = None
    part = ""
    for i in range(len(chaine)):
        if chaine[i] is not p:
            part = part + chaine[i]
        else:
            liste.append(part)
            part = ""
            space_indice = i
    liste.append(chaine[space_indice + 1:len(chaine)])
    return liste


ma_liste = split_("Ama va à l'école")
print(ma_liste)
