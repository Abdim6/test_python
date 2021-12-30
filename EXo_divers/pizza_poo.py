"EXO SUR POO - PIZZA"

# class pizza:
#     def __init__(self, nom):
#        self.nom =nom 
#        self.prix_marg = "7€" 
#        self.prix_4fro = "9€"  
#        self.prix_poulet = "10.5€"  

#     def presenter(self):
#         if(self.nom  == "Marguerita"):
#             print(f"Vous avez pris la pizza : {self.nom}, et elle coùte {self.prix_marg}.")
#         if(self.nom  == "Poulet roti"):
#             print(f"Vous avez pris la pizza : {self.nom}, et elle coùte {self.prix_poulet}.")
#         if(self.nom  == "4 fromages"):
#             print(f"Vous avez pris la pizza : {self.nom}, et elle coùte {self.prix_4fro}.")

#     def menu():
#         print("Voici le Menu des pizzas : ")
#         print("La Pizza Marguerita : 7€.")
#         print("La Pizza Poulet roti : 10.5€.")
#         print("La Pizza 4 fromages : 9€.")

# class pizz_perso (pizza):
#     def __init__(self,ingredients):
#         self.ingredients = ingredients

# print(pizza.menu())
# Choix_pizza = input("Bonjour Pizza Italien, Faites vos choix : ")
# monchoix = pizza(Choix_pizza)
# print(monchoix.presenter())


class pizza:
    def __init__(self, nom, ingredients, prix, vege=False):
       self.nom = nom  
       self.ingredients = ingredients
       self.prix = prix
       self.vege = vege

    def afficher(self):
        str_vege=""
        if self.vege: 
            str_vege = " - Vegeterienne"
        print(f"PIZZA {self.nom} : {self.prix}€"+str_vege)
        print(self.ingredients)
        print("")

class pizzas_perso(pizza):
    prix_base = 5
    prix_par_ingredient = 1.2
    dernier_num = 0
    def __init__(self):
        pizzas_perso.dernier_num+=1
        "Y'A MOYEN DE CREER UNE INSTANCE DE CETTE CLASSE POUR POUVOIR L'UTILISER DANS LES METHODES"
        # self.num= pizzas_perso.dernier_num
        super().__init__("Personnalisée " +str(pizzas_perso.dernier_num),[],0)
        self.faire_choix()
        self.calcul_prix()
        

    def faire_choix(self):
        print(f"Pour la Pizza perso num {pizzas_perso.dernier_num}.")
        while True :
            choix = input(f"Ajoute un ingredient : ")
            if choix == "":
                return
            self.ingredients.append(choix) 
            print(f"L'ingredient {choix} est ajouté.")
    def calcul_prix(self):
        self.prix = pizzas_perso.prix_base + len(self.ingredients)*pizzas_perso.prix_par_ingredient
                       


pizzas = [
    pizza("Maguerita",("fromage", "sauce", "tomate", "champignon"), 7, True),
    pizza("Maguerita2",("fromage", "sauce", "tomate", "champignon"), 9.5),
    pizza("Maguerita3",("fromage", "sauce", "champignon"), 8.5),
    pizzas_perso(),
    pizzas_perso()
]
# mapizza = pizza("Maguerita",("fromage", "sauce", "tomate", "champignon"), 7)


for x in pizzas:
    print()
    x.ingredients=", ".join(x.ingredients)
    x.afficher()


"JE comprends pas pk quand je veux afficher la pizza perso seule rien ne s'affiche !!!"
# mapizza = pizzas_perso()
# # mapizza.ingredients = ", ".join(mapizza.ingredients)
# mapizza.afficher()