import random

sujets = ["Toto", "La voisine", "Mme la maire"]
verbes = ["mange", "ment", "pisse"]
complements = ["la bouffe", "la sodomie", "le pouvoir"]



phrases = []
k =1
def rand_phrases():
    for i in range(20):
        rand_sujet = random.randint(0,len(sujets)-1)
        rand_verbe = random.randint(0,len(verbes)-1)
        rand_complement = random.randint(0,len(complements)-1)
        phrase = sujets[rand_sujet]+" "+verbes[rand_verbe]+" " + complements[rand_complement]+"."
        
        if not phrase in phrases:
            phrases.append(phrase)
            # print(i)
            # print(phrase)
            
    return phrases
    # return phrases 
for ph in rand_phrases():
    print(k)
    k+=1
    print(ph)


