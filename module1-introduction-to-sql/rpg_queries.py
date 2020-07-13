import sqlite3

# Connecting to a DB

conn = sqlite3.connect('rpg_db.sqlite3')

cursor = conn.cursor()


'''
- How many total Characters are there?
- How many of each specific subclass?
- How many total Items?
- How many of the Items are weapons? How many are not?
- How many Items does each character have? (Return first 20 rows)
- How many Weapons does each character have? (Return first 20 rows)
- On average, how many Items does each Character have?
- On average, how many Weapons does each character have?

'''
# How many total Characters are there?
q1_statements = """
SELECT count(*)
FROM charactercreator_character;
"""
print(f'Q1 QUERIES: {cursor.execute(q1_statements).fetchall()}')

classes = ['Cleric', 'Figher', 'Mage', 'Nechomancer', 'Theif']
location = ['charactercreator_cleric', 'charactercreator_fighter',
            'charactercreator_mage', 'charactercreator_necromancer',
            'charactercreator_thief']
select = 'SELECT COUNT(*) '
Q2_1 = f'{select} FROM {location[0]}'

Q2_2 = f'{select} FROM {location[1]}'
Q2_3 = f'{select} FROM {location[2]}'
Q2_4 = f'{select} FROM {location[3]}'
Q2_5 = f'{select} FROM {location[4]}'
print('Q2(Cleric class) count :',f'{cursor.execute(Q2_1).fetchall()}')
print('Q2(Fighter class) count :',f'{cursor.execute(Q2_2).fetchall()}')
print('Q2(Mage class) count :',f'{cursor.execute(Q2_3).fetchall()}')
print('Q2(Nechomancer class) count :',f'{cursor.execute(Q2_1).fetchall()}')
print('Q2(Theif class) count:',f"{cursor.execute('SELECT COUNT (*) FROM charactercreator_thief').fetchall()}")
cursor.execute(
    'SELECT COUNT (*) as "Item Amount" FROM armory_item;').fetchall()
Q3 = '''
SELECT count(*)  
FROM armory_item, armory_weapon
WHERE armory_item.item_id = armory_weapon.item_ptr_id;
'''
print(f'Q3 QUERIES: {cursor.execute(Q3).fetchall()}')
Q4 = '''
SELECT 
COUNT(*) as 'Item Count per character'
FROM 
charactercreator_character
INNER JOIN 
charactercreator_character_inventory 
ON 
charactercreator_character.character_id = charactercreator_character_inventory.character_id
GROUP BY
(charactercreator_character_inventory.character_id)
LIMIT 20;
'''
print(f'Q4 QUERIES: {cursor.execute(Q4).fetchall()}')

Q5 = '''
SELECT
charactercreator_character.character_id, count(*) as "NumberOwep"
FROM
charactercreator_character
JOIN
charactercreator_character_inventory
ON
charactercreator_character.character_id =
charactercreator_character_inventory.character_id
JOIN
armory_weapon
ON
charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
Group by
charactercreator_character.character_id
LIMIT
20;
'''
print(f'Q5 QUERIES: {cursor.execute(Q5).fetchall()}')

Q7 = '''
SELECT AVG(NumberOwep) as "Average number of Wepons" FROM
(SELECT charactercreator_character.character_id, count(*) as "NumberOwep"
FROM charactercreator_character
JOIN 
	charactercreator_character_inventory 
on
	charactercreator_character.character_id = charactercreator_character_inventory.character_id
JOIN
	armory_weapon
on
	charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
Group by
	charactercreator_character.character_id)
'''
print(f'Q7 QUERIES: Average number of weps' ,f'{cursor.execute(Q7).fetchall()}')

Q6 = '''
SELECT AVG(NumOwep) FROM
	(SELECT count(*) as NumOwep
	FROM charactercreator_character
	JOIN charactercreator_character_inventory
	ON charactercreator_character.character_id = charactercreator_character_inventory.character_id
	GROUP BY charactercreator_character.character_id)
'''
print(f'Q6 QUERIES: Average number of items' ,f'{cursor.execute(Q6).fetchall()}')
