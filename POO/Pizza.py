
class Pizza ():
    def __init__(self, nom, prix,ingredients,vege=False) -> None:
        self.nom = nom
        self.prix = prix
        self.ingredients = ingredients
        self.vege = vege

    def afficher (self):
        print(f"Pizza {self.nom} : {self.prix} €.") 
        print(f"Voici les ingrédients de notre pizza : {', '.join(self.ingredients) }")
        if self.vege == True:
            print("cette pizza est végétarienne!")
        print()

mes_pizzas = [
        Pizza("4 fromages", 8,("emmental","brie","jambon","Saint morey"),True),
        Pizza("Poulet curry", 7.5,("Poulet","Rapé","Sauce blanche"," olives")),
        Pizza("Margueretta", 7,("sauce rouge","Rapé","jambon"))
]

# def classer(e):
#     return e.prix
# mes_pizzas.sort(key = classer)

# for pizza in mes_pizzas:
#     # print(pizza.ingredients)



#     # if "jambon" in pizza.ingredients:
#     pizza.afficher()


    # if not pizza.vege:
    #     pizza.afficher()

class PizzPerso(Pizza):
    prix_base = 7
    prix_ingredient = 1.5
    dernier_num = 0
    def __init__(self) -> None:
        PizzPerso.dernier_num += 1
        self.numero = PizzPerso.dernier_num
        super().__init__("Personnalisée "+ str(self.numero), 0, [])
        # self.ingredients = ingredients
        self.ajouter_ingresdients()
        self.calculer_prix ()

    def ajouter_ingresdients(self):
        while True :
            # self.numero +=1
            ingredient = input(f"Ajouter des ingredients pour la pizza N° {self.numero} : ")
            if ingredient == "":
                return
            self.ingredients.append(ingredient)
            print(",".join(self.ingredients))
            # self.prix = 3*len(self.ingredients)
    def calculer_prix (self):
        self.prix = PizzPerso.prix_base + len(self.ingredients)*PizzPerso.prix_ingredient

# mapizza = PizzPerso()
# mapizza.afficher()
nb = 3 
liste_pizza = []
for i in range(3):
    print(f"--- Pizza {i+1} ---")
    liste_pizza.append(PizzPerso())

for i in range(len(liste_pizza)):
    # liste_pizza[i].nom = liste_pizza[i].nom + " " + str(i+1) 
    liste_pizza[i].afficher()


