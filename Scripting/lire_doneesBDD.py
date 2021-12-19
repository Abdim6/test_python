import sqlite3


con=sqlite3.connect("album2.db")
curseur = con.cursor()

curseur.execute("SELECT * FROM artistes")
mes_artistes = curseur.fetchall()

print(mes_artistes)
curseur.close