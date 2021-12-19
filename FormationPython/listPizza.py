
# List_pizza = ["hawai", "4 Frommages", "calzone", "Poulet curry", "Saumon" ]

# ajout_pizza = input("Pizza à ajouter : ")
# List_pizza.append(ajout_pizza)
# print("------ LISTE DES PIZZAS "+"("+str(len(List_pizza))+")"+" ------")

# List_pizza.sort()

# for pizza in List_pizza:
#     print(pizza)
# print()
# print("Première pizza :",List_pizza[0])
# print("Dernière pizza :",List_pizza[-1])



from typing import Collection


def ajouter_pizza(collection):
    ajout_pizza = input("Pizza à ajouter : ")
    for pizza in collection:
        if pizza == ajout_pizza:
            print("La pizza existe déjà")
            print()
            return ajouter_pizza(collection)
    collection.append(ajout_pizza)

def afficher_pizza(collection,n=len(Collection)):
    print("------ LISTE DES PIZZAS "+"("+str(len(collection))+")"+" ------")
    collection.sort()
    if collection ==[]:
        print("La liste est vide")
        return
    for i in range(0,n):
        print(collection[i])
    print()
    print("Première pizza est :", collection[0])
    print("Dernière pizza est :", collection[-1])


List_pizza = ["hawai", "4 Frommages", "calzone", "Poulet curry", "Saumon" ]

ajouter_pizza(List_pizza)
afficher_pizza(List_pizza)
# print(List_pizza)


#tri personnalité
# def tri_perso(list):
#     return len(list)

# Collection.sort(key=tri_perso)