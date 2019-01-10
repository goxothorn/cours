import sqlite3, os, time, time_perso, json, requests
import pandas
## création de la base de donnée##
conn = sqlite3.connect("DB_Audience.db")

## importation des données depuis des .csv en objet pandas
data01 = pandas.read_csv("Test21.csv", header = 0,  sep = ",")
data02 = pandas.read_csv("Test22.csv", header = 0,  sep = ",")

## on pousse les différent fichier csv dans des tables de la base de donnée
data01.to_sql("audience01", conn, if_exists = "replace", index = False)
data02.to_sql("audience02", conn, if_exists = "replace", index = False)
data02.to_sql("audiencemerged", conn, if_exists = "replace", index = False)

## on commit les changements et on ferme la base de donnée
conn.commit()
conn.close()

conn = sqlite3.connect("DB_Audience.db")
cursor = conn.cursor()




