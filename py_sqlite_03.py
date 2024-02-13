import sqlite3

database_name = 'tvrtka.db'
insert_into_table_query = '''
    INSERT INTO employees (last_name, first_name, email)
    VALUES  (?, ?, ?)
'''

employees = [
    ('Peric', 'Pero', 'pero.peric@email.com'),
    ('Anic', 'Ana', 'ana.anic@email.com'),
    ('Ivic', 'Iva', 'iva.ivic@email.com'),
    ('Maric', 'Marko', 'marko.maric@email.com')
]


try:
    sqlite_connection = sqlite3.connect(database_name)
    cursor = sqlite_connection.cursor()

    for employee in employees:
        cursor.execute(insert_into_table_query, employee)    
    
    # COMMIT Stvarna pohrana izmjena stanja podataka u bazi
    sqlite_connection.commit()
    
    cursor.close()

except sqlite3.Error as sql_error:
    print(f'Dogodila se SQLite greska {sql_error}')

except Exception as ex:
    print(f'Dogodila se greska {ex}')

finally:
    if sqlite_connection:
        sqlite_connection.close()
