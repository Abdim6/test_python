"LISTE DE PIZZAS"

class Pizza ():
    def __init__(self, nom,ingredients,prix) -> None:
        self.nom=nom
        self.prix=prix
        self.ingredients = ingredients
    def afficher_pizza(self):
        print(f"Pizza {self.nom} : {self.prix}€.")
        print(self.ingredients)
    
class PizzaPerso (Pizza) : 
    ingredients = []
    def __init__(self, nom, ingredients="", prix=0):
        super().__init__(nom, ingredients, prix=0)
        # PizzaPerso.ingredients=ingredients

    def choisir_ingred(self):
        print("Ingredients pour pizza personnalisée ")
        ingr = ""
        while True:
            ingr = input("Ajouter un ingredient (ou ENTER pour finir) : ")
            if ingr=="":
                break
            PizzaPerso.ingredients.append(ingr)



mapizza=Pizza("haiwienne", ("x","y","z"),9.5)
mapizza.ingredients = ", ".join(mapizza.ingredients)
mapizza.afficher_pizza()

piz = PizzaPerso("Perso")
piz.choisir_ingred()
piz.afficher_pizza()