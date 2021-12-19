import json
# sérialiser & desérealiser 

personne = {"prenom" : "abdi",
            "nom" : "bileh",
            "amis" : ["Ali", "Sophie","Said"]
}

# data -> text (JSON) : sérialiser  dumps
# test (JSON) -> data : desérialiser  loads

personne_json = json.dumps(personne)
print("Mes données JSON : ",personne_json)
"ECRITURE"
# fichierdonnees = open("fichierdonnees","w")
# fichierdonnees.write(personne)
"Pour écrire dans un fichier, faut que les données soit sous forme de string. Ou bien utiliser le données en JSON"
# fichierdonnees.write(personne_json)
# fichierdonnees.close
"LECTURE"
f = open("fichierdonnees","r")
donnees = f.read()
mesdonnees=json.loads(donnees)
"Faut absolument desérialiser ses données avant de vouloir les afficher"
print("Mes données desérialiser :",mesdonnees)
print("-----")
print("Le Nom : ", mesdonnees["nom"])
f.close