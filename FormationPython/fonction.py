
# pip3 list --outdated
# pip3 list



# "utiliser 'f' dans les inputs "
# nb1=1
# nb2=9
# Nb_int=0
# while(True):
#     Nb_str = input(f"Rentrer un chiffre entre {nb1} et {nb2} : ")
#     try:
#         if(Nb_int>=nb2):
#             Nb_int = int(Nb_str)
#         break
#     except:
#         if(Nb_int >nb2):
#             print(f"Rentrer BIEN un chiffre entre {nb1} et {nb2} : ")
#         else:
#             print("Rentrer un chiffre svp")

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


# def choixpersonne(nbmin,nbmax):
#     nb_str=input("rentrer un nb "+str(nbmin)+"et"+str(nbmax)+":")
#     try:
#         nb_int=int(nb_str)
#         if not nbmin<=nb_int<=nbmax:
#             print("Rentrer un nb entre ",nbmin,"et",nbmax)
#             return choixpersonne(nbmin,nbmax)
#         return nb_int
#     except:
#         print("Erreur, rentrer un nombre")
#         return choixpersonne(nbmin,nbmax)

# choix = choixpersonne(1,4)
# print("le choix est :", choix)
# """
# """
# def multitab(n):
#     for i in range(10):
#         print(i, "*", n, "=", i*n)
#     print()

# def addtab(n):    
#     for i in range(10):     
#         print(i, "+", n, "=", i+n)


# def tab(n,x,ope_cbk):   
#     for i in range(10):     
#         print(i, x, n, "=", ope_cbk(i,n))

# def produit_cbk (a,b):
#     return a*b
# def add_cbk (a,b):
#     return a+b 
# def power_cbk(a,b):
#     return pow(a,b)

# tab(9,"+", lambda a,b:a+b)
# print()
# tab(9,"*",lambda a,b:a*b)
# print()
# tab(3,"^", lambda a,b:pow(a,b))

def infos_personne():
    nom = input("Rentre ton nom :")
    age = input("Rentre ton age : ")
    return nom, age
mon_nom, mon_age = infos_personne()
print(f"Vos infos perso : {mon_nom} et {mon_age}")