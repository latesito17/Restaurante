import sqlite3
from database import conectar_db


def registrar_cliente(nombre, direccion, telefono):
    conn = conectar_db()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO clientes (nombre, direccion, telefono) VALUES (?, ?, ?)",
                       (nombre, direccion, telefono))
        conn.commit()
    except sqlite3.IntegrityError as e:
        print(f"Error al registrar cliente: {e}")
    finally:
        conn.close()


def mostrar_clientes():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes")
    return cursor.fetchall()


def eliminar_cliente(cliente_id):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clientes WHERE id=?", (cliente_id,))
    conn.commit()
    conn.close()
