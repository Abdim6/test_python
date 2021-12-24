import sys
""""
                    "comprendre mon erreur"
matab=[]
def mapetitecollection():
    for i in range(10):
        matab[i]=i
        print(matab[i])
    return matab [i]

print(mapetitecollection())
matab.append(15)
print(mapetitecollection)
                    "comprendre mon erreur"


mytab = ["ali","abdi","jean","alex"]
for i in range(0,4):
    print(mytab[i])
x=mytab.append("az")
print(mytab)
print("-------------")
print(mytab[::-1])

print("-------------")

def obtenirinfoperso():
    return "majid", 21,1.7

def afficher(perso, age, taille):
    print("Information : perso :",perso, age , taille)

personne1=obtenirinfoperso()
afficher(*personne1)


print("-------------")




                "Exercice : utilisation des collections"
#prob de version de python - il faut une version 3.5
noms = []
while True:
    nom = input("Saisir un nom : ")
    if nom == "":
        break
    noms.append(nom)
print(noms)


                #exo distance 
Distance_voisin = [1.8, 3, 2.1, 0.7, 20, 4.1]
nom_chauffeur = ["alain", "maria", "Bileh", "bobo", "Li"]
Distancemin=Distance_voisin[0]
index_num = 0
for i in range(len(Distance_voisin)):
    if Distance_voisin[i]<Distancemin:
        Distancemin = Distance_voisin[i]
        index_num=i
print(Distancemin)

print(index_num)
print(nom_chauffeur[index_num])


"QUESTIONNAIRE - sujet les fonctions"
score = 0
def poser_question(question, r1,r2,r3,r4, choix_bonne_reponse):
    global score
    print("QUESTION")
    print(" "+ question)
    print(" (a) ",r1)
    print(" (b) ",r2)
    print(" (c) ",r3)
    print(" (d) ",r4)
    print()
    reponse = input("Votre reponse : ")
    if reponse == choix_bonne_reponse:
        print("Bonne reponse")
        score = score + 1
    else:
        print("Mauvaise reponse")

poser_question("Quelle est la capitale de la France ?", "Marseille", "Paris","Lyon", "Lille","b")
poser_question("Quelle est la capitale de l'Italie ?", "Rome", "Paris","Dijon", "Naples","a")

print("Votre score est : ", score)


"QUESTIONNAIRE - sujet les collections"
score = 0


def poser_question1(question):
    titre_question = question[0]
    Choix_reponse = question[1]
    reponse_attendu = question[2]
    global score

    print("QUESTION")
    print(" "+ titre_question)
    for i in range(len(Choix_reponse)):
        print(i+1," ", Choix_reponse[i])
    # print(" (a) ",question[1][0])
    # print(" (b) ",question[1][1])
    # print(" (c) ",question[1][2])
    # print(" (d) ",question[1][3])
    print()
    reponse_str = input("Choisir une reponse entre 1 et "+str(len(Choix_reponse)) + " : ")
    reponse_int = int(reponse_str) 
    reponse=Choix_reponse[reponse_int-1]
    if reponse.lower() == reponse_attendu.lower():
        print("Bonne reponse")
        score = score + 1
    else:
        print("Mauvaise reponse")

question1 = ("Quelle est la capitale de la France ?", ("Marseille", "Paris","Lyon", "Lille"),"Paris")
question2 = ("Quelle est la capitale de l'Italie ?", ("Roma", "Paris","Dijon", "Naples"),"Roma")

poser_question1(question1)
poser_question1(question2)
# print(question1[1][2])
print("Votre score est : ", score)
"""

"boucle"

# maCondition=True
# age =0
# while(maCondition):
#     try:
#         age=int(input("Rentrer ton age ? : "))
#         break
#     except :
#         print("Votre votre age correctement svp ? ")
#     print("Ton age est : ", age)

# dico = {"nom" : "abdi", "age":"22", "job":"Informaticien","pays":"France"}
# for i in dico:
#     print(dico[i])

x=0
y =1
total = 0
for x in range(100):
    print(total)
    x=y
    y=total
    total=x+y