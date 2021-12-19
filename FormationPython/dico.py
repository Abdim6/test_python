            # VERSION 1
# my_dico = {"Nom": "alice","age":18,"Taille":1.67}

# my_dico ["Nom"] = "Martine"
# achat = ("chocolat","banane","Jus")
# my_dico ["achat"] = achat

# my_dico["poste"]="QA"

# # print(my_dico)

# for i in my_dico:
#     # print(i)
#     # print(my_dico[i])
#     print(f"la clé : {i} - la valeur : {my_dico[i]}")

    #        "VERSION 2"
"recherche des données via liste de donnée => trop lent lorsque la liste en question est trop longue"
# personnes = [
#     ("Alain",30,1.82),
#     ("Tony",40,1.72),
#     ("Charlotte",24,1.86),
#     ("Abdi",35,1.74)
# ]
# def obtenir_personne(liste,nom):
#     for i in personnes:
#         if i[0] == nom:
#             # print(f"La personne recherchée est :{i}")
#             return i 
#     return None
# Infos = obtenir_personne(personnes,"abdi")
# print(f"La personne recherchée est :{Infos}")

                # "Version 3"
"recherche des données via Dictionnaire de donnée =>  très efficace et rapide"
Persoonnes_dico = {
    "Alain" : (30,1.82),
    "Tony" : (40,1.72),
    "Charlotte" : (24,1.86),
    "Abdi" : (35,1.74)
}

# info_dico = Persoonnes_dico["Abdi"]
info_dico = Persoonnes_dico.get("abdi")
print(f"La personne recherchée est : {info_dico}")

# ####### comment connaitre le fonctionnent des fonction ou des attribut natif de pyton, par exemple la fonction get() de dico