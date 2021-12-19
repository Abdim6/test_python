import random

sujets = ["Toto", "La voisine", "Mme la maire", "Mon coloc","Chéri"]
verbes = ["mange", "ment", "pisse","me dérange","aime"]
complements = ["la bouffe", "la sodomie", "le pouvoir","sans arret","toujours"]



def rand_phrases():
    phrases = []
    for i in range(5):
        rand_sujet = random.randint(0,len(sujets)-1)
        rand_verbe = random.randint(0,len(verbes)-1)
        rand_complement = random.randint(0,len(complements)-1)
        phrase = sujets[rand_sujet]+" "+verbes[rand_verbe]+" " + complements[rand_complement]+"."
        print(phrase)
        print(i)
        phrases.append(phrase)
    return phrases
    # return phrases 
print(rand_phrases())

