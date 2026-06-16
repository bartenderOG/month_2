import sqlite3

# Эксемпляр А4
conn = sqlite3.connect('test.db')
# Рука и карандаш
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS users(
        name VARCHAR (30) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
''')
conn.commit()

# CRUD - Create - Read - Update - Delete

def create_user(name, age, hobby):


#     c.execute(
#         'INSERT INTO users(name, age, hobby) VALUES(?, ?, ?)',
#         (name, age, hobby)
#     )
#
#     НЕПРАВИЛЬНО!!!!
#     c.execute(f'INSERT INTO users(name, age, hobby) VALUES ("{name}", "{age}", "{hobby}")')
    conn.commit()
    print('User created successfully')
#
# create_user("Bekzhan", 22, "алкоголь")



def get_users():
    c.execute('SELECT * FROM users')
    data = c.fetchall()
    print(data)
#
# get_users()

def update_users(name, rowid):
    c.execute(
        'UPDATE users SET name = ? WHERE rowid = ?',
        (name, rowid)
    )

conn.commit()
print('User updated successfully:')

# update_users('Vasiliy',2 )


def delete_users(rowid):
    c.execute('DELETE FROM users WHERE rowid = ?', (rowid,))
    conn.commit()
    print('User deleted successfully')

delete_users(1)

