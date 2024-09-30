import sqlite3
from database import conectar_db


def registrar_pago(cliente_id, monto, fecha):
    with conectar_db() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO pagos (cliente_id, monto, fecha) VALUES (?, ?, ?)",
                       (cliente_id, monto, fecha))
        conn.commit()


def mostrar_pagos():
    with conectar_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pagos")
        return cursor.fetchall()


def buscar_pagos_por_cliente(cliente_id):
    with conectar_db() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM pagos WHERE cliente_id = ?", (cliente_id,))
        return cursor.fetchall()
