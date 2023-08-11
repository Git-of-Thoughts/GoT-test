import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect(':memory:') # create a database connection to a SQLite database in memory
        return conn
    except Error as e:
        print(e)

def get_customer(id):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM customers WHERE id=?", (id,))
    rows = cur.fetchall()
    return rows

def add_customer(customer):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO customers(name,email,phone,address) VALUES(?,?,?,?)", (customer['name'], customer['email'], customer['phone'], customer['address']))
    conn.commit()
    return cur.lastrowid

def update_customer(id, customer):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("UPDATE customers SET name=?, email=?, phone=?, address=? WHERE id=?", (customer['name'], customer['email'], customer['phone'], customer['address'], id))
    conn.commit()
    return cur.rowcount

def delete_customer(id):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM customers WHERE id=?", (id,))
    conn.commit()
    return cur.rowcount

def get_interaction(id):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM interactions WHERE id=?", (id,))
    rows = cur.fetchall()
    return rows

def add_interaction(interaction):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO interactions(customer_id,date,notes) VALUES(?,?,?)", (interaction['customer_id'], interaction['date'], interaction['notes']))
    conn.commit()
    return cur.lastrowid

def update_interaction(id, interaction):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("UPDATE interactions SET customer_id=?, date=?, notes=? WHERE id=?", (interaction['customer_id'], interaction['date'], interaction['notes'], id))
    conn.commit()
    return cur.rowcount

def delete_interaction(id):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM interactions WHERE id=?", (id,))
    conn.commit()
    return cur.rowcount
