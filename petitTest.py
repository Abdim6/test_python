# class mere:
#     def __init__(self):
#         pass
#     def afficher(self):
#         print("mere")


# class fille(mere):
#     def __init__(self):
#         super().__init__()

#     def afficher(self, age):
#         # return super().afficher()
#         # print("toto")
#         print(f"je m'appelle toto et j'ai {age} ans.")
#         pass


# x =fille()
# x.afficher(11)
"EXercice 1 : vérifier si un nombre est premeir"
"EXercice 2 : dessiner un triangle"
"https://waytolearnx.com/2020/02/questions-dentretiens-python-partie-7.html?"

# def fonction_plusieurs_var(chaine, to, ki, zcd):
#     for var in chaine: 
#         print(var)

# matab = ("toto","jean", 3, "mouz")
# fonction_plusieurs_var(**matab)

noms = ["toto","amandine","Abdirahman", "Sophie", "momo"]
# noms.sort(key= lambda x:len(x))
# liste = sorted(noms)
# print(noms)
# print(liste)
"ce code est ultra simplifié pour afficher une liste"
masortie = [len(x) for x in noms]

# masortie = [len(x) if len(x)<10 else 0 for x in noms]
# print(masortie)

a = [3,6,9]
b = [1,0,5]
c = a.extend(b)
# print(a)
# print(b)

tuple = (("jo", 22),("toto",21),("ali", 19))

dicto = dict((a,b) for a,b in tuple)
# print(dicto)

une = "chaine"
# une[len(une) ] ='k'
# print(une)

import random
tabo = []
for i in range(10):
    if i <5:
        x = random.randint(97, 122)
    elif 4<i<7:
        x = random.randint(48, 59)
    elif 6<i:
        x = random.randint(84, 122)
    tabo.append(chr(x))
    
# print(tabo)
# print("Le mot de passe est :", "".join(tabo))


# print(chr(97))

import math

print(dir(math.__file__))