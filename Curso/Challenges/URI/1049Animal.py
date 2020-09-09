one = str(input())
two = str(input())
three = str(input())

if one in "vertebrado":
    if two in "ave":
        if three in "carnivoro":
            print("aguia")
        elif three in "onivoro":
            print("pomba")
    elif two in "mamifero":
        if three in "onivoro":
            print("homem")
        elif three in "herbivoro":
            print("vaca")
elif one in "invertebrado":
    if two in "inseto":
        if three in "hematofago":
            print("pulga")
        elif three in "herbivoro":
            print("lagarta")
    elif two in "anelideo":
        if three in "hematofago":
            print("sanguessuga")
        elif three in "onivoro":
            print("minhoca")
