import sqlite3

def drop_table():
    with sqlite3.connect('fifty_sound.db') as con:
        try:
            c = con.cursor()
            c.execute("""DROP TABLE IF EXISTS FIFTY_SOUND;""")
            return True
        except Exception as ex:
            print(ex)


def create_table():
    with sqlite3.connect('fifty_sound.db') as con:
        try:
            c = con.cursor()
            c.execute(
            """
                CREATE TABLE FIFTY_SOUND (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    pron VARCHAR(3) UNIQUE NOT NULL,
                    hiragana VARCHAR(2) UNIQUE NOT NULL,
                    katagana VARCHAR(2) UNIQUE NOT NULL
                )
            """)
            return True
        except Exception as ex:
            print(ex)

if __name__ == '__main__':
    drop_table()
    create_table()
