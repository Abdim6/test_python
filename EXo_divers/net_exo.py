"Exercie trouvés sur le net"

# data = input("rentre des nombre")
# print(data)
# data_tab = data.split(",")
# data_tup = tuple(data_tab)
# print(data_tab)
# print(data_tup)

# from datetime import date


"-----Between two dates----"

# date1 =input("rentre une date 1 : ")
# date2 =input("rentre une date 2 : ")

# print(date(date2) -date(date1))

# def calcul_dif(dat1, dat2):
#     dat_split1 = dat1.split("/")
#     dat_split2 = dat2.split("/")

#     total_jour1 = int(dat_split1[0]) + int(dat_split1[1])*30 + int(dat_split1[2])*360
#     total_jour2 = int(dat_split2[0]) + int(dat_split2[1])*30 + int(dat_split2[2])*360

#     dif = total_jour2 - total_jour1

#     return str(dif) + " jours."

# print("la différence est : ",calcul_dif(date1, date2))

import random

"exo d'écrire tous les chaine de caractere possible"
car = ['a','e','i','o']
car2 = [4,9,23,7,0]
# matab = []
# i=0
# while(True):
   
#     random.shuffle(car)
#     mix = "".join(car)
#     if mix not in matab:
#         i+=1
#         matab.append(mix)
#         print(mix)
#     elif i==2^(len(car)) :
#         print(i)
#         break


# car2_ = car2[0:3]
# print(car2_[::-1])

"---- Remplir un dictionnaire ----"
# mon_dico = dict()
# x_list = [2,6,0,2,11,6,6,0]
# for i in x_list:
#     if i in mon_dico:
#         mon_dico[i] +=1
#     else:
#         mon_dico[i] = 1
# print(mon_dico)

# dico_puissance = dict()
# tab1 = [2,3,4,6,7,8]
# tab2 = [4,9,16,3,36,49,63]


        # resul = zip(tab1,tab2)
        # resul_set = set(resul)
                    
        # print(resul_set)
        # zip


r_list = [1,3,7,98,0]
d_list = []
d_dico = {"nono":7,"emma":98,"abdi":1,"jojo":7,"toto":2}

for x in d_dico:
    if d_dico[x] not in d_list:
        # print(d_dico[x])
        d_list.append(d_dico[x])
print(d_list)