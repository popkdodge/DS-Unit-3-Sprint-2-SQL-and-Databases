import sqlite3

# STEP 1 - connect to a database

conn = sqlite3.connect('demo.sqlite3')
conn

cursor = conn.cursor()

# STEP 2 - make a cursor
'''Now we need to have a table to query
We're going to write SQL as a Python String
This is the main programic flow for the week.'''

create_statement = '''
            CREATE TABLE pizza (name varchar(30), size int, pepperoni int,
            pineapple int);

'''
# STEP 3 - Execute our statements
cursor.execute(create_statement)
cursor.execute('Select * from pizza;').fetchall()

# insert statements
insert_statements = 'INSERT INTO pizza (name, size, pepperoni, pineapple) VALUES ("ellios", 9, 1, 0);'
cursor.execute(insert_statements)
print(cursor.execute('SELECT * FROM pizza;').fetchall())

# Now step 4, close the curseor
cursor.close()
# _____________________________________________________

# Step 5, commit to the database
conn.commit()
