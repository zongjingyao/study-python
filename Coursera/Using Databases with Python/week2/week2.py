import sqlite3
import re

conn = sqlite3.connect('week2.sqlite')
cur = conn.cursor()

fh = open('mbox.txt')
for line in fh:
    if not line.startswith('From ') : continue
    org = re.findall('@(\S+)', line)[0]
    print org
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count) VALUES ( ?, 1 )''', ( org, ) )
    else : 
        cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?', (org, ))
conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

print
print "Counts:"
for row in cur.execute(sqlstr) :
    print str(row[0]), row[1]

cur.close()