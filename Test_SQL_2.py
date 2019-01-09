import sqlite3, os, time, time_perso, json, requests
import pandas

conn = sqlite3.connect("DB_Audience.db")
data01 = pandas.read_csv("Test21.csv", header = 0,  sep = ",")
data02 = pandas.read_csv("Test22.csv", header = 0,  sep = ",")

data01.to_sql("audience01", conn, if_exists = "replace", index = False)
data02.to_sql("audience02", conn, if_exists = "replace", index = False)
data02.to_sql("audiencemerged", conn, if_exists = "replace", index = False)

conn.commit()
conn.close()

conn = sqlite3.connect("DB_Audience.db")
cursor = conn.cursor()




