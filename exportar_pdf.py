import sqlite3
from fpdf import FPDF
from pagos_controller import mostrar_pagos


def exportar_pagos_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pagos = mostrar_pagos()
    for pago in pagos:
        pdf.cell(
            200, 10, txt=f"ID: {pago[0]}, Cliente ID: {pago[1]}, Monto: {pago[2]}, Fecha: {pago[3]}", ln=True)

    pdf.output("pagos.pdf")
