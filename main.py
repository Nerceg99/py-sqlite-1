# 1. Korak - import sqlite3 modul
import sqlite3

# 2. Korak - kreirati SQL Upit
sql_query = 'SELECT sqlite_version()'

try:
    # 3. Korak - kreiranje konekcije na bazu
    sqlite_connection = sqlite3.connect('tvrtka.db')

    # 4. Korak - kreiranje cursor objekta/interface
    cursor = sqlite_connection.cursor()

    # 5. Korak - uporaba kursor objekta za rad s podacima u bazi podataka
    cursor.execute(sql_query)
    records = cursor.fetchall()
    cursor.close()

    print(f'Sadrzaj records objekta: {records}')

except sqlite3.Error as sql_error:
    print(f'Dogodila se SQLite greska {sql_error}')

except Exception as ex:
    print(f'Dogodila se greska {ex}')

finally:
    if sqlite_connection:
        sqlite_connection.close()
        print('SQLite konekcija je zatvorena\n')
