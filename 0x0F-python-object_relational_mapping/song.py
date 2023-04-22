#!/usr/bin/python3
import MySQLdb
db = MySQLdb.connect(host='localhost', user='esayyas', passwd='password', db='hbtn_0e_0_usa')
cur = db.cursor()
cur.execute("CREATE TABLE song ( id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, title TEXT NOT NULL )")
songs = ('Purple Haze', 'All Along the Watch Tower', 'Foxy Lady')
for song in songs:
    cur.execute("INSERT INTO song (title) VALUES (%s)", song)
    print "Auto Increment ID: %s" % cur.lastrowid
cur.execute("SELECT * FROM song WHERE id = %s or id = %s", (1,2))
numrows = cur.execute("SELECT * FROM song")
print "Selected %s rows" % numrows
print "Selected %s rows" % cur.rowcount
