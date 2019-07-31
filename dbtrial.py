import sqlite3

conn=sqlite3.connect('chatbot.db')

print("Connection successful!")

#conn.execute('''CREATE TABLE USER_ENTRIES
#         (QUOTE VARCHAR(50))''')

"""
conn.execute('''CREATE TABLE USER_ENTRIES
         (ID INT PRIMARY KEY     NOT NULL,
         PRONOUN           VARCHAR(50)    NOT NULL,
         VERB        VARCHAR(50)     NOT NULL,
         NOUN        VARCHAR(50));''')
"""
"""
conn.execute("INSERT INTO USER_ENTRIES (ID,PRONOUN,VERB,NOUN) \
      VALUES (1, 'Paul', 'HELLO', 'California' )");
"""

"""
cursor = conn.execute("SELECT id, pronoun, verb, noun from USER_ENTRIES")
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("ADDRESS = ", row[2])
"""

#conn.execute("INSERT INTO USER_ENTRIES(quote)\
#        VALUES ('Hello how are you')")
#Input in single quotes since inside double quotes.

cur = conn.cursor()
cur.execute("SELECT quote from USER_ENTRIES")
#print(list(cursor)) Output: []
#cursor is a SQLITE object
#row is a tuple with each element as each column input
rows = cur.fetchall() #VERY IMPORTANT else will create a new empty database and erase old contents. http://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/
for row in rows:
    print("Response: ", row[0])


print("Table created successfully")

conn.close()
