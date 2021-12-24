import requests
from bs4 import BeautifulSoup

"Scrapy : un framework qui nous permet de recolter des données sur le net!"
recette = open("recette.html","r")
"le contenu de la page dans une variable"
html_content = recette.read()
recette.close()
"Parcourir le contenu récupéré"
soup = BeautifulSoup(html_content,"html.parser")
titre = soup.find("h1")
description = soup.find("p")
# print(titre.text)
# print(description)

"""Dans des fichier/page HTML plus complex, on aura besoin de plus spécifier la balise qu'on souhaite retourner,
 par ce qu'il peut y avoir des conflit de balise de meme nom"""

div_info = soup.find("div", class_="info")
img_info = div_info.find("img")

# print(div_info.img)
print(img_info["src"])



"""
Pour aller plus loin y'a une formation sur udemy,
Tu peux t'entrainer d'avantage avec d'autres sites.
"""