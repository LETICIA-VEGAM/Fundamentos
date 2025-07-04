from tkinter import *
from tkinter import ttk

def calcular(*args):
    try:
        valor = float(pies.get())
        metros.set((0.3048 * valor * 10000.0 + 0.5) / 10000.0 )
    except ValueError:
        pass

raiz = Tk()
raiz.title("Pies a metros")

marcoPrincipal = ttk.Frame(raiz, padding="3 3 12 12")
marcoPrincipal.grid(column=0, row=0, sticky=(N, W, E, S))
marcoPrincipal.columnconfigure(0, weight=1)
marcoPrincipal.rowconfigure(0, weight=1)

pies = StringVar()
metros = StringVar()

