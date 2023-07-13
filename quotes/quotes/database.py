
# For practice this file is not use in this project
import sqlite3

conn = sqlite3.connect('myquote.db')
curr = conn.cursor()

# Creating the table
# curr.execute("""create table quotes_tb(
#                 title text,
#                 author text,
#                 tag text)""")


# Inserting in the table
curr.execute("""insert into quotes_tb values('Python', 'Abhishek Negi', 'Programing Language')""")
conn.commit()
conn.close()
