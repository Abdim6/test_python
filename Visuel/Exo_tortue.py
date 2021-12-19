import turtle

t = turtle.Turtle()

def construction_escalier(taille,nbMarche):
    for i in range(0,nbMarche):
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)
    # t.forward(taille)

construction_escalier(30,8)

# def construire_carre(taille):
   
#         for i in range(0,4):
#             t.forward(taille)
#             t.left(90) 
        
# def construire_carres(taille_depart, nb):
#     for j in range(0,nb):
#         taille = (j+1)*taille_depart
#         construire_carre(taille)
#     print(taille)    

# construire_carres(25,6)
# construire_carre(29)

"ceci permet de garder la fenetre ouverte"
turtle.done() 