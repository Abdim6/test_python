"Utiliser des fichiers"

monfichier = open("nombre2.txt","w")
print("Vous pouvez écrire dans le fichier, pour finir faites Entrer.")
while(True):
    Donnee_saisi = input("Ecrire quelques choses d'utile pour l'humanité : ")
    if Donnee_saisi != "":
        monfichier.write(Donnee_saisi+"\n") 
    else:
        break

    # for i in range(15):
    #     monfichier.write("\n" + str(i))



# try:
#     monfichier = open("nombre2.txt","r")
#     lecture = monfichier.readlines()
#     # print(lecture)
#     # print("\n".join(lecture))
#     for line in lecture:
#         print(line, end="")
#     monfichier.close()
# except FileNotFoundError :
#     print("Erreur!")

