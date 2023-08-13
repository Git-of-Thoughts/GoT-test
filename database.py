import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('game.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS scores (
                id INTEGER PRIMARY KEY,
                ip TEXT,
                country TEXT,
                score INTEGER
            )
        ''')

    def update_score(self, user, score):
        self.cursor.execute('''
            INSERT INTO scores (ip, country, score)
            VALUES (?, ?, ?)
        ''', (user.ip, user.country, score))
        self.conn.commit()

    def get_ranking(self, country):
        self.cursor.execute('''
            SELECT * FROM scores
            WHERE country = ?
            ORDER BY score DESC
        ''', (country,))
        return self.cursor.fetchall()
