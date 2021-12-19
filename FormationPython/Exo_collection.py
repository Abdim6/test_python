"Exo collection "


# noms = ["kAder","faTou","binta","marIe","alEX"]


# trouve = False
# def element_dans_liste (nom, liste):
    # global trouve
    # for el in liste:
    #     if nom.lower() == el.lower():
    #         return True     
    # return False

                        # "IMPORTANT A SAVOIR"
#     liste_lower = [el.lower() for el in liste]
#     return nom.lower() in liste_lower
    
# # def element_dans_liste(nom, liste):
# #     return nom in liste

# rep = element_dans_liste("maRie", noms)
# # print(rep)

# if(rep):
#     print("Trouvé")
# else:
#     print("Non trouvé!")



fichiers = ("notepad.exe","mon.fichier.perso.doc","notes.TXT","vacances.jpeg","planing","data.dat")


definition_extensions=(("doc","Document word"),
                       ("exe", "Exécutable"),
                       ("txt","Document texte "),
                       ("jpeg", "Images JPEG"))

fichiers
x = fichiers[3].split("e")
print(x)

# def trouve_extension(liste):
#     for fichier in fichiers:
#         if "." in fichier:
#             # print()
#             ext = fichier.split(".")
#             # print(ext)
#             extension = combine_ext(ext[-1])
#             # print(ext[-1])
#             print(fichier, "(", extension, ")")
#             # return ext[-1]
#         else:
#             print(fichier, "(Pas d'extension)")
#             # return False

# def combine_ext(ext):
#     for i in range(len(definition_extensions)):
#         if ext.lower() == definition_extensions[i][0].lower():
#             return definition_extensions[i][1]
#     return "Extension pas connue"


# ext_trouve = trouve_extension(fichiers)
# print(ext_trouve)
# # print(combine_ext("exe"))


# fichiers2 = ["notepad.exe","mon.fichier.perso.doc","notes.TXT","vacances.jpeg","planing","data.dat"]
# noms2 = ["kAder","faTou","binta","marIe","alEX","zOo"]


# def calculer_nb_caracter(liste):
#     nb_car=0 
#     for var in liste:
#         nb_car+=len(var)
#     return nb_car

# def calculer_nb_caracter2(liste):
#     maliste=[]
#     for var in liste:
#         maliste.append(len(var))
#     return sum(maliste)

# tous_tous_noms = "".join(fichiers2)
# print(tous_tous_noms)
# print(len(tous_tous_noms))

# nombre_caractere1 = calculer_nb_caracter(fichiers2)
# nombre_caractere2 = calculer_nb_caracter(noms2)
# nombre_caractere21 = calculer_nb_caracter2(fichiers2)
# nombre_caractere22 = calculer_nb_caracter2(noms2)

# print(nombre_caractere1)
# print(nombre_caractere2)
# print()
# print(nombre_caractere21)
# print(nombre_caractere22)
