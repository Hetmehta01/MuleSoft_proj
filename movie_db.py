import sqlite3
connection = sqlite3.connect('fav_movies.db')
cursor = connection.cursor()

cursor.execute
table = (''' create table if not exists Movies2
(Movie varchar(100), Lead_actor varchar(100), Lead_actress varchar(100), Year int, director varchar(100))
''')
cursor.execute(table)

cursor.execute('''INSERT INTO Movies2 VALUES ('3 idiots', 'Aamir Khan', 'Kareena Kapoor', '2009', 'Hirani')''')
cursor.execute('''INSERT INTO Movies2 VALUES ('Golmaal Returns', 'Ajay Devgan', 'Pareneti Chopra', '2018', 'Rohit Shetty')''')
cursor.execute('''INSERT INTO Movies2 VALUES ('Airlift', 'Akshay Kumar', 'Raveena Tandon', '2016', 'Hirani')''')
cursor.execute('''INSERT INTO Movies2 VALUES ('Singham', 'Ajay Devgan', 'Kareena Kapoor', '2009', 'Hirani')''')

def disp(query):
    for row in query:
        print(row)

print("Data Inserted in the table: ")
q1 = cursor.execute('''SELECT * FROM Movies2''')
q2 = cursor.execute('''SELECT * FROM Movies2 where Lead_actor = 'Ajay Devgan' ''')
# q3 = cursor.execute(''' delete from Movies2 where Lead_actor = 'Aamir Khan' ''')
disp(q1)


connection.commit()
connection.close()