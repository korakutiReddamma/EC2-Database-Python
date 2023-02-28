import sqlite3
a = sqlite3.connect('data1.db')
b = a.cursor()
b.execute('''SELECT * from data1''')
result = b.fetchall()
print(result)
a.commit()
a.close()