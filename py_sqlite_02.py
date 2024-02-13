import sqlite3


create_table_query = '''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    last_name TEXT NOT NULL,
    first_name TEXT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT
);
'''

try:
    sqlite_connection = sqlite3.connect('tvrtka.db')
    cursor = sqlite_connection.cursor()

    cursor.execute(create_table_query)
    cursor.close()

except sqlite3.Error as sql_error:
    print(f'Dogodila se SQLite greska {sql_error}')

except Exception as ex:
    print(f'Dogodila se greska {ex}')

finally:
    if sqlite_connection:
        sqlite_connection.close()
