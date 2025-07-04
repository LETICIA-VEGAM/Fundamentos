import tkinter as tk
from tkinter import ttk

def convertir(*args):
    try:
        pies = float(entrada_pies.get())
        metros = pies * 0.3048
        etiqueta_resultado.config(text=f"{metros:.4f} metros")
    except ValueError:
        etiqueta_resultado.config(text="Por favor ingresa un número válido.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Conversor de Pies a Metros")

# Configurar la cuadrícula
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=3)

# Etiqueta de instrucción
ttk.Label(ventana, text="Ingresa pies:").grid(column=0, row=0, padx=10, pady=10)

# Entrada de texto
entrada_pies = ttk.Entry(ventana)
entrada_pies.grid(column=1, row=0, padx=10, pady=10)
entrada_pies.focus()  # Enfocar al inicio

# Botón para convertir
boton_convertir = ttk.Button(ventana, text="Convertir", command=convertir)
boton_convertir.grid(column=0, row=1, columnspan=2, padx=10, pady=10)

# Etiqueta de resultado
etiqueta_resultado = ttk.Label(ventana, text="Resultado en metros")
etiqueta_resultado.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

# Asociar la tecla Enter a la función convertir
ventana.bind("<Return>", convertir)

# Iniciar el bucle de la aplicación
ventana.mainloop()