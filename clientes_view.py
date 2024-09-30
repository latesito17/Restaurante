import tkinter as tk
from tkinter import messagebox, ttk
from cliente_controller import registrar_cliente, mostrar_clientes, eliminar_cliente


def ventana_clientes():
    ventana = tk.Toplevel()
    ventana.title("Registrar Cliente")
    ventana.geometry("400x400")

    # Frame para el contenido
    marco = tk.Frame(ventana)
    marco.pack(pady=20)

    # Label y Entry para nombre
    label_nombre = tk.Label(marco, text="Nombre:")
    label_nombre.pack(pady=10)

    entry_nombre = tk.Entry(marco)
    entry_nombre.pack(pady=10)

    # Label y Entry para dirección
    label_direccion = tk.Label(marco, text="Dirección:")
    label_direccion.pack(pady=10)

    entry_direccion = tk.Entry(marco)
    entry_direccion.pack(pady=10)

    # Label y Entry para teléfono
    label_telefono = tk.Label(marco, text="Teléfono:")
    label_telefono.pack(pady=10)

    entry_telefono = tk.Entry(marco)
    entry_telefono.pack(pady=10)

    # Función para registrar el cliente
    def registrar():
        nombre = entry_nombre.get()
        direccion = entry_direccion.get()
        telefono = entry_telefono.get()

        registrar_cliente(nombre, direccion, telefono)
        messagebox.showinfo("Éxito", "Cliente registrado con éxito.")
        ventana.destroy()

    # Botón para registrar el cliente
    btn_registrar = tk.Button(
        marco, text="Registrar Cliente", command=registrar)
    btn_registrar.pack(pady=20)

    # Función para eliminar cliente
    def eliminar_cliente_ventana():
        clientes = mostrar_clientes()
        cliente_seleccionado = combo_cliente.get()
        if cliente_seleccionado:
            cliente_id = cliente_seleccionado.split(" (ID: ")[1][:-1]
            eliminar_cliente(cliente_id)
            messagebox.showinfo("Éxito", "Cliente eliminado con éxito.")
            ventana.destroy()

    # Combobox para seleccionar cliente a eliminar
    clientes = mostrar_clientes()
    combo_cliente = ttk.Combobox(
        marco, values=[f"{cliente[1]} (ID: {cliente[0]})" for cliente in clientes])
    combo_cliente.pack(pady=10)

    btn_eliminar = tk.Button(
        marco, text="Eliminar Cliente", command=eliminar_cliente_ventana)
    btn_eliminar.pack(pady=20)


def ventana_lista_clientes():
    ventana = tk.Toplevel()
    ventana.title("Lista de Clientes")
    ventana.geometry("400x400")

    # Frame para la tabla
    marco = tk.Frame(ventana)
    marco.pack(pady=20)

    # Treeview para mostrar la lista de clientes
    tree = ttk.Treeview(marco, columns=(
        "ID", "Nombre", "Dirección", "Teléfono"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Nombre", text="Nombre")
    tree.heading("Dirección", text="Dirección")
    tree.heading("Teléfono", text="Teléfono")
    tree.pack()

    # Obtener y agregar clientes a la tabla
    clientes = mostrar_clientes()
    for cliente in clientes:
        tree.insert("", tk.END, values=cliente)

    # Botón para cerrar la ventana
    btn_cerrar = tk.Button(marco, text="Cerrar", command=ventana.destroy)
    btn_cerrar.pack(pady=10)
