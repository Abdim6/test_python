            #En passant par les FONCTIONS
# i=0
# def choix_capitale(question, r1,r2,r3,r4,r5,Choix):
#     global i 
#     print(question)
#     print(" 1 - ",r1)
#     print(" 1 - ",r2)
#     print(" 1 - ",r3)
#     print(" 1 - ",r4)
#     print(" 1 - ",r5)
#     reponse = input("Choisir une de ces propositions : ")
#     print()
#     if reponse != Choix:
#         print("Mauvaise reponse")
#         return
#     print("Bonne reponse")
#     i+=1
    


# choix_capitale("Quelle est la capitale de la france ?", "Lyon","Paris","Nice","Marseille","Lille","Paris")
# choix_capitale("Quelle est la capitale de l'Espagne", "Madrid","Paris","Nice","Barcelone","Lille","Paris")
# choix_capitale("Quelle est la capitale de l'italie", "Lyon","Paris","Rome","Vénise","Parme","Rome")
# print(f"Votre score est : {i}")


                #avec LA COLLECTION 
score=0
def questionnaire(question):
    global score
    titre_question = question[0]
    choix_reponse = question[1]
    print(titre_question)
    for i in range(len(choix_reponse)): 
        print(f" ({i+1}) - {choix_reponse[i]}")
    print()
    rep = Saisir_le_choix_num(1,len(choix_reponse))
    if question[1][rep-1] == question[2]:
        print("Bonne reponse")
        score+=1
    else:
        print("Mauvaise reponse")
    print()
    

def Saisir_le_choix_num(min,max):
    choix_rep_str = input(f"Choisir le num correspondant de la bonne reponse (entre {min} et {max}) : ")
    # choix_rep_int = int(choix_rep_str)
    try:
        choix_rep_int = int(choix_rep_str)
        if min<=choix_rep_int<=max:
            return choix_rep_int
        else :
            print("Faut saisir un nombre valide svp")
    except:
        print("Veuillez rentrer un chiffre")
    return Saisir_le_choix_num (min,max)




question1 = ("Quelle est la capitale de la france ?", ("Lyon","Paris","Nice","Marseille","Lille"),"Paris")
question2 = ("Quelle est la capitale de l'Espagne ? ", ("Madrid","Paris","Nice","Barcelone","Lille"),"Madrid")
question3 = ("Quelle est la capitale de l'italie ?", ("Lyon","Paris","Rome","Vénise","Parme"),"Rome")

questionnaire(question1)
questionnaire(question2)
questionnaire(question3)
print(f"Votre score est : {score}")
