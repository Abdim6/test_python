#les tubles on peut pas ajouter des nouveaux elements : immutable ()
#la liste on peut ajouter des elements : mutable ajouter / supprimer []


#afficher une liste de nom dans liste 

# personne =[]
# while True :
#     nom = input("Ajouter un nom dans la liste : ")
#     if nom !="":
#         personne.append(nom)
#     else:
#         break
# print(personne)
# for nom in personne:
#     print(nom.capitalize())
#     print()


# chauffure = ["jo", "paul","ali","mina","marie","fatou"]
# Distance = [1.2,5,2.8,1,18,6.8]
# chauffure_distance = [("abdi",2.1),("mehdi",0.9),("Jean",1.9)]

# distance_min = chauffure_distance[0]
# print(distance_min)
# for distance_nb in chauffure_distance:
#     if distance_nb[1]<distance_min[1]:
#         distance_min=distance_nb
 
# print(distance_min)


# k=0
# j=Distance[0]
# for i in Distance:
#     if i<j:
#         j=i
#         i=Distance[k]
# print(j)
# print(k)
                # "-------------------NOTIONS AVANCES-----------------------"

noms = ["toto","patate","Sauce","Ali","Ordi"]
print(noms)
noms.append("ajout")    
print(noms)
noms_sup = ["abdi","momo"]
noms.extend(noms_sup)
print(noms)
noms.insert(3,"dji")
print(noms)

"Slice [:] => crée une copie de la liste sans altérer cette denière"

"liste.sort() => modifie la liste en faisant l'ordre // sorted(liste) => une autre liste est crée"
# liste.sort(reverse = True)
# liste.sort(key=lambda x : len(x), reverse = True)  => appelé inplace
# print(min(liste)) //  print(max(liste))