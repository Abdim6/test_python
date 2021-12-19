
# # Create a sample collection
# users = {'Hans': 'active', 'eleonore': 'inactive', 'master': 'active'}

# # Strategy:  Iterate over a copy
# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]
#         print("mon print : ",user)
#         print("mon print : ",status)


# "PAS COMPRIS LE FONCTIONNEMENT DES COLLECTIONS"

# # Strategy:  Create a new collection
# active_users = {}
# for user, status in users.items():
#     if status == 'active':
#         active_users[user] = status



# a = ['Mary', 'had', 'a', 'little', 'lamb']
# for i in range(len(a)):
#     print(i, a[i])

for num in range(1, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        break
    print("Found an odd number", num)


# def fib(num):
#     a=0
#     b=1
#     print("----Suite de fibonnaci-----")
#     while(a<num):
#         print(a)
#         a=b
#         b=a+b
# fib(100)      


# def fib(n):    # write Fibonacci series up to n
#     a = 0
#     b = 1
#     libe = []
#     while a < n:
#         libe.append(a)
#         a, b = b, a+b
#     return libe

# print(fib(100))


# def f(a, L=[]):
#     L.append(a)
#     return L

# print(f(1))
# print(f(2))
# print(f(3))

# def f(a, L=None):
#     if L is None:
#         L = []
#     L.append(a)
#     return L
# print(f(1))
# print(f(2))
# print(f(3))

# "Ajout d'un element dans une liste"
# a = ["a", 5, 89, "moi",True]
# print(a)
# print(len(a))
# a[len(a): ]= ["x"]
# print(a)
# a.insert(0,"Premier")
# print(a)
# a.remove(5)
# print(a)
# valeur = a.pop(3)
# print(valeur)


# "La methode range() est utile dans les boucles for"
# maListe = []
# for x in range(5):
#     maListe.append(x*x)
# print(maListe)

# "fonction for utilisee dans une liste"
# uneliste = [0, 6, 9, 2, 17,1]
# listedeux = [x*2 for x in uneliste]
# print(listedeux)



# "la fonction zip est geniale, elle transpose une liste de liste"
# Matrix = [
#     [2,6,0,'y'],
#     ["a",7,3,'x'],
#     [8,4,0,9],
# ]

# Matrix2 = list(zip(*Matrix))
# print(Matrix2)


# "une boucle for peut etre utilisee dans une dico, via l afonction items()"
# Dicto = {'apple':4 , 'orange': 'apple', 'pear': 'orange', 1: 'banana'}
# print(Dicto) 
# for x,y in Dicto.items():
#     print (x,y)



# "Pour faire une boucle sur une sequence de maniere ordonnee, utilisez la fonction sorted(), pour eliminer le doublon combine avec set()"
# basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# for i in sorted(basket):
#     print(i)


# "ceci est un module"
# import sys
# print(dir(sys))


# "la fonction format utilisee dans les prints pour afficher des inputs"
# for x in range(1, 11):
#     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))


# class Complex:
#     def __init__(self, realpart, imagpart):
#         self.r = realpart
#         self.i = imagpart

# x = Complex(3.0, -4.5)
# print(x.r, x.i)

# print("---------")
# x.counter = 1
# while x.counter < 17:
#     x.counter = x.counter * 2
# print(x.counter)
# del x.counter


# class Employee:
#    'Common base class for all employees'
#    empCount = 0

#    def __init__(self, name, salary):
#       self.name = name
#       self.salary = salary
#       Employee.empCount += 1
   
#    def displayCount(self):
#      print ("Total Employee : %d" % Employee.empCount)

#    def displayEmployee(self):
#       print ("Name : ", self.name,  ", Salary: ", self.salary )

# x = Employee("abdi",30)
# y = Employee("bibi",27)
# Employee.displayCount(x)
# Employee.displayEmployee(x)

# print(Employee.__name__)



# class Parent:        # define parent class
#    parentAttr = 100
#    def __init__(self):
#       print ("Calling parent constructor")

#    def parentMethod(self):
#       print ('Calling parent method')

#    def setAttr(self, attr):
#       Parent.parentAttr = attr

#    def getAttr(self):
#       print ("Parent attribute :", Parent.parentAttr)

# class Child(Parent): # define child class
#    def __init__(self):
#       print ("Calling child constructor")

#    def childMethod(self):
#       print ('Calling child method')


# voisin=Parent()
# voisin.parentMethod()
# voisin.setAttr("la famille")
# voisin.getAttr()
# print("-------")
# bebe=Child()
# bebe.parentMethod()