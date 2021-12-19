   
#                     # VERSION FONCTION 

# i=0
# def questionnaire(titre_question, r1,r2,r3,r4,Choix_rep):
#     global i
#     print("Questions : ")
#     print(titre_question)
#     print(  "a - ",r1)
#     print(  "b - ",r2)
#     print(  "c - ",r3)
#     print(  "d - ",r4)
#     print()
#     Choix_rep_rentre=input()
#     if Choix_rep_rentre==Choix_rep:
#         print("bonne reponse")
#         i+=1
#     else:
#         print("Erreur!")
    

# questionnaire("Quelle est la capitale de laFrance", "Nice","Paris","Londre","Rome","b")
# questionnaire("Quelle est la capitale de l'Italie", "Nice","Paris","Londre","Rome","d")
# print("Votre score est :",i,"/ 2")

# --------------

# questionnaire_dico = {
#     "Quelle est la capitale de la France?" : (("Nice","Paris","Londre","Rome"), "Paris"),
#     "Quelle est la capitale de l'Italie?" : (("Nice","Paris","Londre","Rome"), "Paris"),
#     "Quelle est la capitale de la Belgique?" : (("Nice","Bruxelle","Londre","Rome"), "Paris")
# }

# for cap in questionnaire_dico:
#     print(questionnaire_dico[cap])
# ---------------
# i=0
# questionnaire_tuple=(
#     (("Quelle est la capitale de la France?"),  ("Nice","Paris","Londre","Rome"), ("Paris")),
#     (("Quelle est la capitale de l'Italie?"), ("Nice","Paris","Londre","Rome"), ("Rome")),
#     (("Quelle est la capitale de la Belgique?"), ("Nice","Bruxelle","Londre","Rome"), ("Bruxelle"))
# )

# for i in questionnaire_tuple:
#     print(i[0])
#     for j in questionnaire_tuple[1]:
#         print (f" (a) - {j}.")
#     reponse = input ()
#     if reponse==i[2]:
#         print("bonne reponse")
#         i+=1
#     else:
#         print("Erreur!")

                            # QUESTION CAPITALES VERSION COLLECTIONS
i=0
def poser_question(question):
    global i
    nb = len(question[1])
    print(f"Choisi la bonne reponse entre 1 et {nb} : ")
    print(question[0])
    for j in range(len(question[1])):
        # print(" ",j)
        print(f" {j+1} - {question[1][j]}")
    # print(  "a - ",question[1][0])
    # print(  "b - ",question[1][1])
    # print(  "c - ",question[1][2])
    # print(  "d - ",question[1][3])
    print()
    Choix_rep_rentre=input("Votre reponse : ")
    index_reponse = question[1][int(Choix_rep_rentre) - 1]
               # --------- reponse en string -----------
    # if Choix_rep_rentre.lower() == question[2].lower():
    #     print("bonne reponse")
    #     i+=1
    # else:
        # print("Erreur!")
        # --------- reponse en Int -----------
    if index_reponse == question[2]:
        print("bonne reponse")
        i+=1
    else:
        print("Erreur!")

question1 = ("Quelle est la capitale de la France", ("Nice","Paris","Londre","Rome","Djibouti"),"Paris")
question2 = ("Quelle est la capitale de l'Italie", ("Nice","Paris","Djibouti","Rome"),"Rome")


poser_question(question1)
poser_question(question2)
print("Votre score est :",i,"/ 2")