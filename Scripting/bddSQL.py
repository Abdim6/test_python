from os import curdir
import sqlite3
from sqlite3.dbapi2 import Cursor

# LANGAGE SQL
# -----------

# INTEGER : int
# VARCHAR : str

# artiste
# - artiste_id
# - nom

# album
# - album_id
# - artiste_id
# - titre
# - annee_sortie

# CREATE TABLE artiste (
#     artiste_id INTEGER NOT NULL PRIMARY KEY, 
#     nom VARCHAR);
"ajouter references artiste, pour notifier que cette donnée est partagée dans l'autre tab"
# CREATE TABLE album (
#     album_id INTEGER NOT NULL PRIMARY KEY, 
#     artiste_id INTEGER REFERENCES artiste,
#     titre VARCHAR,
#     annee_sortie INTEGER);

# INSERT INTO artiste (nom) VALUES ("Michael Jackson");
# INSERT INTO album (artiste_id, titre, annee_sortie) VALUES (1, "Thriller", 1983);

# UPDATE album SET annee_sortie = 1982 WHERE titre = "Thriller";

# DELETE FROM artiste WHERE nom = "Madonna"
"Select : pour consulter ses données"
# SELECT * FROM artiste
# SELECT nom FROM artiste
# SELECT * FROM album WHERE annee_sortie > 1990;

# SELECT nom, titre FROM album a JOIN artiste ar ON a.artiste_id = ar.artiste_id

# SELECT titre FROM album a JOIN artiste ar ON a.artiste_id = ar.artiste_id AND ar.nom = "Celine Dion"


connexion = sqlite3.connect("Mabasse")


Curseur = connexion.cursor()
# Curseur.execute("""CREATE TABLE artiste (
#         artiste_id INTEGER NOT NULL PRIMARY KEY, 
#         nom VARCHAR);""")

# Curseur.execute("""CREATE TABLE album (
#     album_id INTEGER NOT NULL PRIMARY KEY, 
#     artiste_id INTEGER REFERENCES artiste,
#     titre VARCHAR,
#     annee_sortie INTEGER);""")


# Curseur.execute("""INSERT INTO artiste (nom) VALUES ("Michael Jackson");""")
# Curseur.execute("""INSERT INTO artiste (nom) VALUES ("Celine Dion ");""")
my_donnees1 = []
my_donnees1 = Curseur.execute("""INSERT INTO album (artiste_id, titre, annee_sortie) VALUES (1, "Thriller", 1983);""")
my_donnees2 = Curseur.execute("""INSERT INTO album (artiste_id, titre, annee_sortie) VALUES (1, "Falling into you", 1996);""")

print(my_donnees1)
print(my_donnees2)

connexion.commit()
connexion.close()


