text = """
Écrivez un script qui compte dans un fichier texte quelconque le nombre de lignes contenant des caractères numériques.
ecrivez un script qui compte le nombre de mots contenus dans un fichier texte.
ecrivez un script qui recopie un fichier texte en veillant à ce que chaque ligne commence par une majuscule.
Abdi
"""
"exo 2"
fichier_test = open("fichier_test.txt","r")

contenu_fichier = fichier_test.readlines()
# fichier_test2.write(text)

fichier_test2 = open("fichier_test.txt","w")
# longueur_lignes=0
# for ch in contenu_fichier:
#     longueur_lignes +=len(ch)
#     print(ch, end="")
# print(longueur_lignes)


"exo 3"
for ch in contenu_fichier:
    ch1 = ch[0].upper()
    print(ch1)
    chs = ch[1:]
    print(chs)
    chaine = ch1+chs
    fichier_test2.write(chaine)
   


"exo 1"
# for ch in contenu_fichier:
#     if "j" in ch:
#         print(ch, end="")
#         # print(ch[0])



fichier_test.close