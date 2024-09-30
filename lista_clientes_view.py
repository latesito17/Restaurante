import tkinter as tk
from tkinter import messagebox
from cliente_controller import mostrar_clientes


def ventana_lista_clientes():
    ventana = tk.Toplevel()
    ventana.title("Lista de Clientes")
    ventana.geometry("400x400")

    # Frame para el contenido
    marco = tk.Frame(ventana)
    marco.pack(pady=20)

    # Obtener y mostrar clientes
    clientes = mostrar_clientes()
    for cliente in clientes:
        cliente_info = f"ID: {cliente[0]}, Nombre: {cliente[1]}, Dirección: {cliente[2]}, Teléfono: {cliente[3]}"
        label_cliente = tk.Label(marco, text=cliente_info)
        label_cliente.pack(pady=5)
