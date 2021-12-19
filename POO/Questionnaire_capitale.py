


# POO
"""
=> Une classe question.
=> Une classe questionnaire qui hérite classe question. 
=> Methode poser question (afficher).
=> Rentrer la réponse à la question + calculer le score.
=> Des attrébuts (titre).
=> 


"""




class Questions ():
    def __init__(self,titre,choix,reponse) -> None:
        self.titre = titre
        self.choix = choix
        self.reponse = reponse 
    def poser_question(self):
        # reponse = False
    # titre_question = question[0]
    # choix_reponse = question[1]
        print(self.titre)
        for i in range(len(self.choix)): 
            print(f" ({i+1}) - {self.choix[i]}")
        print()
        rep = Questions.Saisir_le_choix_num(1,len(self.choix))
        if self.choix [rep-1] == self.reponse:
            print("Bonne reponse")
            return True
            # score+=1
        else:
            print("Mauvaise reponse")
        print()
        return False

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
        return Questions.Saisir_le_choix_num (min,max)

class Questionnaire():
    def __init__(self, questions) -> None:
        self.questions = questions
    def lancer(self):
        score = 0
        for q in self.questions:
            if q.poser_question():
                score +=1
        print("Score final :", score, "sur", len(self.questions))




Questionnaire((
    Questions("Quelle est la capitale de la france ?", ("Lyon","Paris","Nice","Marseille","Lille"),"Paris"),
    Questions("Quelle est la capitale de l'Espagne ? ", ("Madrid","Paris","Nice","Barcelone","Lille"),"Madrid"),
    Questions("Quelle est la capitale de l'italie ?", ("Lyon","Paris","Rome","Vénise","Parme"),"Rome")
)).lancer()

# q1.poser_question()



# score=0
# def questionnaire(question):
#     global score
#     titre_question = question[0]
#     choix_reponse = question[1]
#     print(titre_question)
#     for i in range(len(choix_reponse)): 
#         print(f" ({i+1}) - {choix_reponse[i]}")
#     print()
#     rep = Saisir_le_choix_num(1,len(choix_reponse))
#     if question[1][rep-1] == question[2]:
#         print("Bonne reponse")
#         score+=1
#     else:
#         print("Mauvaise reponse")
#     print()
    

# def Saisir_le_choix_num(min,max):
#     choix_rep_str = input(f"Choisir le num correspondant de la bonne reponse (entre {min} et {max}) : ")
#     # choix_rep_int = int(choix_rep_str)
#     try:
#         choix_rep_int = int(choix_rep_str)
#         if min<=choix_rep_int<=max:
#             return choix_rep_int
#         else :
#             print("Faut saisir un nombre valide svp")
#     except:
#         print("Veuillez rentrer un chiffre")
#     return Saisir_le_choix_num (min,max)




# question1 = ("Quelle est la capitale de la france ?", ("Lyon","Paris","Nice","Marseille","Lille"),"Paris")
# question2 = ("Quelle est la capitale de l'Espagne ? ", ("Madrid","Paris","Nice","Barcelone","Lille"),"Madrid")
# question3 = ("Quelle est la capitale de l'italie ?", ("Lyon","Paris","Rome","Vénise","Parme"),"Rome")

# questionnaire(question1)
# questionnaire(question2)
# questionnaire(question3)
# print(f"Votre score est : {score}")
