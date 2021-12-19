

class personne():
    def __init__(self,nom="", age=0) -> None:
        self.nom=nom
        self.age=age
        if self.nom == "":
            self.nom = input("Merci de rentrer votre nom : ")
    def se_presenter(self):
        
        if self.age!=0:
            print("Je m'appelle "+ self.nom,", et j'ai ",self.age,"ans.")
            if(self.estmajeur()):
                print("Je suis majeur")
            else :
                print("Je suis mineur")
        else:
            print("Je m'appelle "+ self.nom)
        # print("Estmajeur : ", self.estmajeur())

    def estmajeur(self):
        if (self.age>=18):
            return True
        else:
            return False
    
personne1 = personne(age=20)

personne1.se_presenter()
# print("Estmajeur : "+str(personne1.estmajeur()))



