import sqlite3


def conectar_db():
    """Conectar a la base de datos y devolver la conexión."""
    return sqlite3.connect('cocina_oculta.db')


def crear_base_de_datos():
    """Crear las tablas necesarias en la base de datos."""
    conn = conectar_db()
    cursor = conn.cursor()

    # Eliminar la tabla anterior si existe
    cursor.execute("DROP TABLE IF EXISTS clientes")

    # Crear tabla sin el campo correo
    cursor.execute('''
    CREATE TABLE clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        direccion TEXT NOT NULL,
        telefono TEXT NOT NULL UNIQUE
    )
    ''')

    conn.commit()
    conn.close()

# Llamar a la función para crear la base de datos (descomentar la siguiente línea si necesitas crear la base de datos)
# crear_base_de_datos()
