import sqlite3

"on va créer une nouvelle base de donnée"
"Puis on va la consulter"
    # "executer/curseur"
    # "Commit"
    # "fermer"

con=sqlite3.connect("album2.db")
sql_tab_artistes = """CREATE TABLE artistes (
    artiste_id INTEGER NOT NULL PRIMARY KEY, 
    nom VARCHAR,
    annee_naissance INTEGER,
    nationnalite VARCHAR);"""
sql_tab_albums = """CREATE TABLE albums (
    album_id INTEGER NOT NULL PRIMARY KEY, 
    titre VARCHAR,
    annee_sortie INTEGER,
    nb_disque INTEGER);"""

sql_tab_artiste1 = """INSERT INTO artistes
    (nom) VALUES ("Michal JACKSON");
"""
sql_tab_artiste2 = """INSERT INTO artistes
    (nom) VALUES ("Céline DION");
"""
sql_tab_artiste3 = """INSERT INTO artistes
    (nom) VALUES ("BOOBA");
"""

"le curseur est un objet intermédiaire pour accéder aux données de la base de données"
"on pourra utiliser ce objet curseur plusieurs fois"

Curseur = con.cursor() 
Curseur.execute(sql_tab_artistes)
Curseur.execute(sql_tab_albums)
Curseur.execute(sql_tab_artiste1)
Curseur.execute(sql_tab_artiste2)
cd_id = Curseur.lastrowid
Curseur.execute(sql_tab_artiste3)
bb_id = Curseur.lastrowid

"L'ajout de données"
Curseur.execute("""INSERT INTO albums
    (album_id,titre,annee_sortie, nb_disque) VALUES ("1","Love me", "1990","50 millions");""")


"Pour gérer l'ID de l'album, on peut utiliser lastrowid"
# Curseur.execute("INSERT INTO albums (album_id,titre,annee_sortie, nb_disque) VALUES ("+ str(cd_id) + ",'In feeling', '1997','112 millions');")

Curseur.execute("""INSERT INTO albums
    (album_id,titre,annee_sortie, nb_disque) VALUES (""" + str(cd_id) + ',"Feeling me", "1998","110 millions");')
    

Curseur.execute("""INSERT INTO albums
    (album_id,titre,annee_sortie, nb_disque) VALUES (""" + str(bb_id) + ',"Friday", "2016","2 millions");')
    
"Le commit nous garantis que les données rentrées soit écrites dans la base de données"
con.commit()
con.close()