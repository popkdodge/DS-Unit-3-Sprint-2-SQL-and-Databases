import sqlite3
import pandas as pd
import numpy as np

# STEP 1 - connect to a database

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
conn

cursor = conn.cursor()
df = pd.read_csv('buddymove_holidayiq.csv')
df.to_sql('buddymove_holidayiq', con=conn)

Q1 = 'SELECT count(*) as Count_of_rows FROM buddymove_holidayiq;'
Q2 = '''
SELECT count(*) as Count_of_rows
FROM buddymove_holidayiq
WHERE Nature >= 100 and Shopping >=100;
'''
Q3_strech = '''
SELECT
round(AVG(Nature),2) as Nature_Avg, round(AVG(Sports),2) as Sport_Avg, round(AVG(Religious),2) as Religion_Avg,
round(AVG(Theatre),2) as Theatre_Avg, round(AVG(Shopping)
        , 2) as Shopping_avg, round(AVG(Picnic),2) as Picnic_AVG
FROM (SELECT * FROM buddymove_holidayiq)
'''
'''
- Count how many rows you have - it should be 249!
- How many users who reviewed at least 100 `Nature` in the category also
  reviewed at least 100 in the `Shopping` category?
- (*Stretch*) What are the average number of reviews for each category?
'''
print('Q1(Count): ', f'{cursor.execute(Q1).fetchall()}')
print('Q2(User with >100 Nature and >100 Shopping): \n',
      f'{cursor.execute(Q2).fetchall()}')
print('Q3(Streach: AVG of all reviews): \n',
      f'{cursor.execute(Q3_strech).fetchall()}')
