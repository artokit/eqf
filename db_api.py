import sqlite3
from sqlite3 import IntegrityError

connect = sqlite3.connect('db.sqlite')
cursor = connect.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS "users" (
	"user_id"	INTEGER NOT NULL UNIQUE,
	"username"	TEXT,
	PRIMARY KEY("user_id")
);""")


def add_user(user_id: int, username: str):
    try:
        cursor.execute("INSERT INTO USERS(user_id, username) VALUES(?, ?)", (user_id, username))
        connect.commit()
    except IntegrityError:
        pass


def get_users():
    return cursor.execute("SELECT * FROM USERS").fetchall()
