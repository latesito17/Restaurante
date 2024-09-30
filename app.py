import tkinter as tk
from tkinter import messagebox
from clientes_view import ventana_clientes
from pagos_view import ventana_pagos
from exportar_pdf import exportar_pagos_pdf
from clientes_view import ventana_clientes, ventana_lista_clientes


def main():
    ventana_principal = tk.Tk()
    ventana_principal.title("Cocina Oculta")
    ventana_principal.geometry("300x300")

    # Botón para abrir ventana de clientes
    btn_clientes = tk.Button(
        ventana_principal, text="Gestionar Clientes", command=ventana_clientes)
    btn_clientes.pack(pady=10)

    # Botón para abrir ventana de pagos
    btn_pagos = tk.Button(
        ventana_principal, text="Registrar Pagos", command=ventana_pagos)
    btn_pagos.pack(pady=10)

    # Botón para exportar pagos a PDF
    btn_exportar_pdf = tk.Button(
        ventana_principal, text="Exportar Pagos a PDF", command=exportar_pagos_pdf)
    btn_exportar_pdf.pack(pady=10)

    # Botón para mostrar lista de clientes
    btn_lista_clientes = tk.Button(
        ventana_principal, text="Lista de Clientes", command=ventana_lista_clientes)
    btn_lista_clientes.pack(pady=20)

    ventana_principal.mainloop()


if __name__ == "__main__":
    main()
