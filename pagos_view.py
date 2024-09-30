import tkinter as tk
from tkinter import messagebox
from pagos_controller import registrar_pago


def ventana_pagos():
    ventana = tk.Toplevel()
    ventana.title("Registrar Pago")
    ventana.geometry("400x400")

    # Frame para el contenido
    marco = tk.Frame(ventana)
    marco.pack(pady=20)

    # Label y Entry para ID del cliente
    label_cliente_id = tk.Label(marco, text="ID Cliente:")
    label_cliente_id.pack(pady=10)

    entry_cliente_id = tk.Entry(marco)
    entry_cliente_id.pack(pady=10)

    # Label y Entry para monto
    label_monto = tk.Label(marco, text="Monto:")
    label_monto.pack(pady=10)

    entry_monto = tk.Entry(marco)
    entry_monto.pack(pady=10)

    # Label y Entry para fecha
    label_fecha = tk.Label(marco, text="Fecha (YYYY-MM-DD):")
    label_fecha.pack(pady=10)

    entry_fecha = tk.Entry(marco)
    entry_fecha.pack(pady=10)

    # Función para registrar el pago
    def registrar():
        cliente_id = entry_cliente_id.get()
        monto = entry_monto.get()
        fecha = entry_fecha.get()

        registrar_pago(cliente_id, monto, fecha)
        messagebox.showinfo("Éxito", "Pago registrado con éxito.")
        ventana.destroy()

    # Botón para registrar el pago
    btn_registrar = tk.Button(marco, text="Registrar Pago", command=registrar)
    btn_registrar.pack(pady=20)
