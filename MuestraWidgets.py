from tkinter import *
from tkinter import ttk

def guardar(*args):
    try:
        print(nombre.get())
    except:
        pass

def cancelar(*args):
    try:
        print("Se borraran los datos capturados")
    except:
        pass

ventanaRaiz = Tk()
ventanaRaiz.title("Muestra de Widgets")

marcoPrincipal = ttk.Frame(ventanaRaiz, padding="10 10 10 10")
marcoPrincipal.grid(column=0, row=0)

marcoDatos = ttk.Frame(marcoPrincipal, relief='raised', padding="25 25 25 25")
marcoDatos.grid(column=0, row=0)

nombre = StringVar()
apPaterno = StringVar()
apMaterno = StringVar()
correo = StringVar()
movil = StringVar()

txtNombre = ttk.Entry(marcoDatos, width=25, textvariable=nombre)
txtNombre.grid(column=1, row=0)
txtApPaterno = ttk.Entry(marcoDatos, width=25, textvariable=apPaterno)
txtApPaterno.grid(column=1, row=1)
txtApMaterno = ttk.Entry(marcoDatos, width=25, textvariable=apMaterno)
txtApMaterno.grid(column=1, row=2)
txtCorreo = ttk.Entry(marcoDatos, width=25, textvariable=correo)
txtCorreo.grid(column=1, row=3)
txtMovil = ttk.Entry(marcoDatos, width=25, textvariable=movil)
txtMovil.grid(column=1, row=4)

ttk.Label(marcoDatos, text="Nombre:").grid(column=0, row=0, sticky=(W))
ttk.Label(marcoDatos, text="A. Paterno:").grid(column=0, row=1, sticky=(W))
ttk.Label(marcoDatos, text="A. Materno:").grid(column=0, row=2, sticky=(W))
ttk.Label(marcoDatos, text="Correo:").grid(column=0, row=3, sticky=(W))
ttk.Label(marcoDatos, text="Móvil:").grid(column=0, row=4, sticky=(W))

marcoOcupacion = ttk.Frame(marcoPrincipal)
marcoOcupacion.grid(column=1, row=0)

ocupacion = StringVar()

estudiante = ttk.Radiobutton(marcoOcupacion, text='Estudiante', variable=ocupacion, value='estudiante').grid(column=1, row=0, sticky=(W))
empleado = ttk.Radiobutton(marcoOcupacion, text='Empleado', variable=ocupacion, value='empleado').grid(column=1, row=1, sticky=(W))
desempleado = ttk.Radiobutton(marcoOcupacion, text='Desempleado', variable=ocupacion, value='desempleado').grid(column=1, row=2, sticky=(W))

marcoAficiones = ttk.Frame(marcoPrincipal, relief="raised")
marcoAficiones.grid(column=0, row=1)

ttk.Label(marcoAficiones, text="Aficiones:").grid(column=0, row=0, sticky=(W))
ttk.Checkbutton(marcoAficiones, text="Leer", width=8).grid(column=0, row=1, sticky=(W))
ttk.Checkbutton(marcoAficiones, text="Música", width=8).grid(column=1, row=1, sticky=(W))
ttk.Checkbutton(marcoAficiones, text="Videojuegos", width=15).grid(column=2, row=1, sticky=(W))

estados = StringVar()

cmbEstados = ttk.Combobox(marcoPrincipal, textvariable=estados)
cmbEstados.grid(column=1, row=1)
cmbEstados['values']=["Aguascalientes", "Zacatecas", "Durango", "Jalisco", "Nayarit", "Mazatlán"]

marcoBotones = ttk.Frame(marcoPrincipal)
marcoBotones.grid(column=0, row=2)

ttk.Button(marcoBotones, text="Guardar", width=15, command=guardar).grid(column=0, row=0, sticky=(W))
ttk.Button(marcoBotones, text="Cancelar", width=15, command=cancelar).grid(column=1, row=0, sticky=(W))

for child in marcoPrincipal.winfo_children():
    child.grid_configure(padx=10, pady=10)

for child in marcoDatos.winfo_children():
    child.grid_configure(padx=10, pady=10)

for child in marcoAficiones.winfo_children():
    child.grid_configure(padx=10, pady=5)

for child in marcoBotones.winfo_children():
    child.grid_configure(padx=10, pady=5)

txtNombre.focus()
ventanaRaiz.bind("<Return>", guardar)

ventanaRaiz.mainloop()