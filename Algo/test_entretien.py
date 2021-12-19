

"Inverser une chaine de caractere"
ma_chaine = "longuement avec fougue"
caratere = []
for i in range(len(ma_chaine)):
    car = ma_chaine[-(i+1)]
    caratere.append(car)
nouv_chaine = " ".join(caratere)
# print(caratere)
# print(nouv_chaine)
# print()
# print(ma_chaine[::-2])

"Trouver le mot le plus long et celui le plus court dans une phrase"
phrase = "Trouver le mot le plus long et celui le plus court dans une phrase que abdirahman a ecrit"
tab = phrase.split(" ")
long = 0
mot1=""
court = 100
mot2 = ""
for i in range(len(tab)):
    if(len(tab[i])>long):
        long = len(tab[i])
        mot1 = tab[i]
    if(len(tab[i])<court):
        court = len(tab[i])
        mot2 = tab[i]
# print("Mot le plus court de la chaine : ",mot2)
# print("Mot le plus long de la chaine : ",mot1)
# print()
# print(tab)

# print("Mot le plus long de la chaine : ",max(tab, key=len))
# print("Mot le plus court de la chaine : ",min(tab, key=len))