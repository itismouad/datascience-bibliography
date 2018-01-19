##################################################
###                                            ###
##   Corrigé du TP 7 sur les bases de données   ##
#                                                #
##       Version du vendredi 6 juin 2014        ##
###                                            ###
##################################################


###### Conncection à la base films.db ######
import sqlite3
conn=sqlite3.connect('films.db')
c=conn.cursor()
############################################


## Question a)
c.execute('SELECT titre FROM film WHERE annee=1974')
print(c.fetchall())

## Question b)
c.execute('SELECT titre FROM film,realisateur WHERE id_realisateur=realisateur.id AND prenom="Akira" AND nom="Kurosawa"')
print(c.fetchall())

## Question c)
c.execute('SELECT titre FROM film,jeu,acteur WHERE id_film=film.id AND id_acteur=acteur.id AND prenom="Jim" AND nom="Carrey"')
print(c.fetchall())

## Question d)
c.execute('SELECT prenom,nom FROM film,jeu,acteur WHERE id_acteur=acteur.id AND id_film=film.id AND titre="Inception"')
print(c.fetchall())

## Question e)
c.execute('SELECT DISTINCT acteur.prenom,acteur.nom FROM film,realisateur,jeu,acteur WHERE id_realisateur=realisateur.id AND id_film=film.id AND id_acteur=acteur.id AND realisateur.prenom="Francis Ford" AND realisateur.nom="Coppola"')
print(c.fetchall())

## Question f)
c.execute('SELECT titre FROM film,jeu,acteur,realisateur WHERE id_film=film.id AND id_acteur=acteur.id AND acteur.prenom="Cary" AND acteur.nom="Grant" AND realisateur.nom="Hitchcock" AND realisateur.prenom="Alfred"')
print(c.fetchall())

## Question g)
c.execute('SELECT prenom,nom,COUNT(*) FROM film,realisateur WHERE id_realisateur=realisateur.id GROUP BY prenom,nom')
print(c.fetchall())

## Question h)
c.execute('SELECT prenom,nom,COUNT(*) AS total FROM jeu,acteur WHERE id_acteur=acteur.id GROUP BY prenom,nom HAVING total>2')
print(c.fetchall())

## Question i)
c.execute('SELECT annee,COUNT(*) AS total FROM film GROUP BY annee ORDER BY total DESC')
print(c.fetchall())

## Question j)
c.execute('SELECT prenom,nom,COUNT(*) AS total FROM realisateur,film WHERE id_realisateur=realisateur.id GROUP BY prenom,nom ORDER BY total DESC')
print(c.fetchall())

## Question k)
c.execute('SELECT prenom,nom,AVG(note) AS moyenne FROM entree,utilisateur WHERE id_utilisateur=utilisateur.id GROUP BY prenom,nom')
print(c.fetchall())

## Question l)
c.execute('SELECT titre,AVG(note) AS moyenne FROM entree,film WHERE id_film=film.id GROUP BY titre ORDER BY moyenne DESC')
print(c.fetchall())