from tkinter import *
from tkinter import ttk

def ingresar(*args):
    try:
        print(usuario.get())
        print(contraseña.get())
    except ValueError:
        pass

ventanaRaiz = Tk()
ventanaRaiz.title("Incio de Sesión")

marcoPrincipal = ttk.Frame(ventanaRaiz,padding="20 20 20 20")
marcoPrincipal.grid(column=0, row=0)

usuario = StringVar()
contraseña = StringVar()

txtUsuario = ttk.Entry(marcoPrincipal, width=30, textvariable=usuario)
txtUsuario.grid(column=1, row=0, sticky=(W))

txtContraseña = ttk.Entry(marcoPrincipal, width=30, textvariable=contraseña)
txtContraseña.grid(column=1, row=1, sticky=(W))

ttk.Label(marcoPrincipal, text="Usuario:").grid(column=0, row=0, sticky=(E))
ttk.Label(marcoPrincipal, text="Contraseña:").grid(column=0, row=1, sticky=(E))

ttk.Button(marcoPrincipal, text="Ingresar", width=15, command=ingresar).grid(column=1, row=2, sticky=(E))

for child in marcoPrincipal.winfo_children():
    child.grid_configure(padx=10, pady=10)
    
txtUsuario.focus()
ventanaRaiz.bind("<Return>", ingresar)

ventanaRaiz.mainloop()