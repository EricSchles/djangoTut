#!/usr/bin/env python
import cgi,cgitb
import sqlite3

cgitb.enable()


print "Content-Type: text/html\n"
print "<html><head><title>Books</title></head>"
print "<body>"
print "<h1>Books</h1>"
print "<ul>"

conn = sqlite3.connect("thing.db")
cur = conn.cursor()
cur.execute("select * from thing")

for row in cur.fetchall():
  print "<li>%s,%s,%s</li>" % (row[0],row[1],row[2])

print "</ul>"
print "</body></html>"

conn.close()
