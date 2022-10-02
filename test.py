import sqlite3

db = sqlite3.connect('nama_database.db')
mycursor = db.cursor()
query = "CREATE TABLE IF NOT EXISTS nama_tabel (nama_kolom1 tipe_kolom1, nama_kolom2 tipe_kolom2);"
mycursor.execute(query)
db.commit()
