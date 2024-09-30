import tkinter as tk
from tkinter import messagebox
from pagos_controller import buscar_pagos_por_cliente
from cliente_controller import mostrar_clientes


def ventana_buscar_pagos():
    ventana = tk.Toplevel()
    ventana.title("Buscar Pagos por Cliente")
    ventana.geometry("400x300")

    # Frame para el contenido
    marco = tk.Frame(ventana)
    marco.pack(pady=20)

    # Label y Combobox para seleccionar cliente
    label_cliente = tk.Label(marco, text="Seleccionar Cliente:")
    label_cliente.pack(pady=10)

    clientes = mostrar_clientes()
    cliente_options = [
        f"{cliente[1]} (ID: {cliente[0]})" for cliente in clientes]

    combo_cliente = tk.ttk.Combobox(marco, values=cliente_options)
    combo_cliente.pack(pady=10)

    # Función para buscar pagos
    def buscar_pagos():
        try:
            cliente_id = int(combo_cliente.get().split(" (ID: ")[-1][:-1])
            pagos = buscar_pagos_por_cliente(cliente_id)
            resultado = "\n".join(
                [f"ID: {pago[0]}, Monto: {pago[2]}, Fecha: {pago[3]}" for pago in pagos])
            messagebox.showinfo(
                "Resultados", resultado or "No se encontraron pagos.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")

    # Botón para buscar pagos
    btn_buscar = tk.Button(marco, text="Buscar Pagos", command=buscar_pagos)
    btn_buscar.pack(pady=20)
