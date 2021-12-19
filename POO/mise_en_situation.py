# # POO EXERCICE DE MISE EN SITUATION 1
# # genre
# #   False : Femme
# #   True  : Homme
# class Personne:
#     def __init__(self, nom: str, age: int, genre: bool):
#         self.nom = nom   # crée une variable d'instance : nom
#         self.age = age
#         self.genre = genre
#         print("Constructeur personne " + self.nom)

#     def SePresenter(self):
#         # Bonjour, je m'appelle Jean, j'ai 30 ans
#         # Je suis majeur
#         print("Bonjour, je m'appelle " + self.nom + ", j'ai " + str(self.age) + " ans")
#         if self.genre:
#             # print("Bonjour, je m'appelle " + self.nom + ", j'ai " + str(self.age) + " ans")
#             print("Genre : Masculin")
#             if self.EstMajeur():
#                 print("Je suis majeur")
#             else:
#                 print("Je suis mineur")
#             print()
#         else:
#         #     print("Bonjour, je m'appelle " + self.nom + ", j'ai " + str(self.age) + " ans")
#             print("Genre : Feminin")
#             if self.EstMajeur():
#                 print("Je suis majeure")
#             else:
#                 print("Je suis mineure")
#             print()

#     def EstMajeur(self):
#         return self.age >= 18

# personne1 = Personne("Jean", 25, True)
# personne1.SePresenter()

# personne2 = Personne("Emilie", 17, False)
# personne2.SePresenter()




"--------------------------"


# # POO EXERCICE DE MISE EN SITUATION 2
# class Personne:
#     def __init__(self, nom: str, age):
#         self.nom = nom   # crée une variable d'instance : nom
#         self.age = age
#         print("Constructeur personne " + self.nom)

#     def SePresenter(self):
#         # Bonjour, je m'appelle Jean, j'ai 30 ans
#         # Je suis majeur
#         print("Bonjour, je m'appelle " + self.nom + ", j'ai " + str(self.age) + " ans")
#         if self.EstMajeur():
#             print("Je suis majeur")
#         else:
#             print("Je suis mineur")
#         print()

#     def EstMajeur(self):
#         return self.age >= 18

# personne1 = Personne("Jean", 16)
# personne1.SePresenter()

# personne2 = Personne("Emilie", 21)
# personne2.SePresenter()


"-------------------------------------"
# POO EXERCICE DE MISE EN SITUATION 3

# ---
# class Chat:
#     def __init__(self, nom_facultatif="inconnu"):
#         self.nom = nom_facultatif

#     def SePresenter(self):
#         print("Bonjour, je suis un chat et je m'appelle " + self.nom)

# # ---
# class Personne:
#     def __init__(self, nom: str):
#         self.nom = nom

#     def SePresenter(self):
#         print("Bonjour, je suis une personne et je m'appelle " + self.nom)

# # ---
# chat1 = Chat()
# chat1.SePresenter()  # Bonjour, je suis un chat et je m'appelle inconnu

# chat2 = Chat("Garfield")
# chat2.SePresenter()  # Bonjour, je suis un chat et je m'appelle Garfield

# personne = Personne("Jean")
# personne.SePresenter()  # Bonjour, je suis une personne et je m'appelle Jean

"MISE EN SITUATION N°4"

class Personne():
    def __init__(self,nom) -> None:
        self.nom=nom
    def sepresenter(self):
        print(f"je m'appelle {self.nom} et ...")

tab = []

for i in range(3):
    tab.append(Personne(input("Rentrer votre nom ? ")))
    
for personne in tab :
    personne.sepresenter()
