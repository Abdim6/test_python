import random

nb_min = 0
nb_max = 10
j=0

def genereNB ():
    nb_random=random.randint(nb_min, nb_max)
    return(nb_random)

def operations ():
    global j

    for i in range(0,4):
        nb_ope=random.randint(0,1)
        print("Question ",i+1," sur 4 :") 
        nb1 = genereNB()
        nb2 = genereNB()
        if nb_ope==0:
            #produit=int(input("Calculer :  {nb_random1}  * {nb_random2}  = ")) 
            print("Calculer : ", nb1 , "*", nb2, " = ")
            produit=devine()
            produit_reel = (nb1 * nb2)
            if(produit==produit_reel):
                print("CORRECT")
                j+=1
            else:
                print("ERREUR!")

        else :
            print( )
            somme=devine()
            somme_reel = nb1 + nb2
            if(somme==somme_reel):
                print("CORRECT")
                j+=1
            else:
                print("ERREUR!")
        print()
    print("Vous avez un score de :", j,"/4.")

def devine():
    while True:
        try:
            nb_devin=int(input())
            break
        except:
            print("Rentrer un nombre valide svp. Réessayer!")
    return nb_devin

operations()

"""

for i in range(0,4):
    nb_random1=random.randint(nb_min, nb_max)
    nb_random2=random.randint(nb_min, nb_max)
    nb_ope=random.randint(0,1)
    print("Question ",i," sur 4 :") 
    if nb_ope==0:
        #produit=int(input("Calculer :  {nb_random1}  * {nb_random2}  = ")) 
        print("Calculer : ", nb_random1 , "*", nb_random2, " = ")
        produit=int(input())
        produit_reel = (nb_random2 * nb_random1)
        if(produit==produit_reel):
            print("CORRECT")
            j+=1
        else:
            print("ERREUR!")

    else :
        print("Calculer : ", nb_random1 , "+", nb_random2, " = ")
        somme=int(input())
        somme_reel = nb_random2 + nb_random1
        if(somme==somme_reel):
            print("CORRECT")
            j+=1
        else:
            print("ERREUR!")
    print()



if(j==4): 
    print("putain! tu es un génie : 4/4")
else:
    print("Vous avez un score de :", j,"/4.")
"""