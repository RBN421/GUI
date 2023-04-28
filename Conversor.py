from tkinter import *
from tkinter import ttk

def calcular(*args):
    try:
        resultado = float(pies.get()) * 0.3048
        metros.set(resultado)
    except ValueError:
        pass

raiz = Tk() #Se crea objeto para agregar la raiz
raiz.title("Pies a Metros")

marcoPrincipal = ttk.Frame(raiz, padding="15 15 15 15") #Se crea objeto para agregar el marco pricipal
marcoPrincipal.grid(column=0, row=0)

pies = StringVar()
metros = StringVar()

txtPies = ttk.Entry(marcoPrincipal, width=7, textvariable=pies, justify="center") # Se crea el objeto para introducir los pies
txtPies.grid(column=1, row=0)

ttk.Label(marcoPrincipal, text="pies").grid(column=2, row=0, sticky=(W)) # Crear objetos de etiquetas con metodo de objetos anonimos
ttk.Label(marcoPrincipal, text="Son equivalentes a:").grid(column=0, row=1, sticky=(E))
ttk.Label(marcoPrincipal, textvariable=metros).grid(column=1, row=1, sticky=(W, E))
ttk.Label(marcoPrincipal, text="metros").grid(column=2, row=1, sticky=(W))

ttk.Button(marcoPrincipal, text="Calcular", command=calcular).grid(column=2, row=2) # Crear objeto de boton con metodo de objetos anonimos

for hijo in marcoPrincipal.winfo_children():
    hijo.grid_configure(padx=5, pady=5)

txtPies.focus()
raiz.bind("<Return>", calcular)

raiz.mainloop()