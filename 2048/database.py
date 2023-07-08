import sqlite3

#подключениие к базе данных
db = sqlite3.connect("2048.sqlite")

#создание таблицы
cur = db.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS records (
    name text,
    score integer
    )
""")


#сохранние новых резултатов по окончании игры в БД
def insert_result(name, score):
    cur.execute("""
        INSERT INTO records VALUES (?, ?)  
    """, (name, score))

    db.commit()


# вывод 3-х лучших результатов для отображения в шапке интерфейса игры
def get_best():
    cur.execute("""
    SELECT name AS master, MAX(score) AS score
    FROM records
    GROUP BY name
    ORDER BY score DESC
    LIMIT 3;
    """)
    return cur.fetchall()
