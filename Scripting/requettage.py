# FAIRE DES APPELS RÉSEAU AVEC REQUESTS
#
# https://codeavecjonathan.com/res/programmation.txt
# https://codeavecjonathan.com/res/pizzas1.json
# https://codeavecjonathan.com/res/exemple.html


import requests
import json
from requests.models import Response
reponse1 = requests.get("https://codeavecjonathan.com/res/programmation.txt")
reponse1.encoding = "uft-8"
"Affichage du contenu texte du lien"
# print(reponse1.text)


reponse2 = requests.get("https://codeavecjonathan.com/res/pizzas1.json")
reponse2.encoding = "uft-8"
# print(reponse2.text)
# print(type(reponse2.text))

"Desérialiser les données importées depuis un site web"
"C'est comme ça qu'on fait lorsqu'on communique avec une API REST, cette API nous permet de récupérer des données sous forme JSON"
mondico = json.loads(reponse2.text)
for dic in mondico:
    print(dic)
print(type(mondico))
print(len(mondico))

"------"
"Telechargement d'images"
"Le but ici est recupérer une image depuis un site, puis l'enregistrer dans un fichier sous forme binaire"
recup = requests.get("https://codeavecjonathan.com/res/papillon.jpg")
mon_image = open("Papillon.jpg","wb")

mon_image.write(recup.content)
mon_image.close()