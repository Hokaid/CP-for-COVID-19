from tkinter import *
from tkinter import ttk
from data_visualize import *
from CPmodel import *

raiz = Tk() 
raiz.title("COVID-19 PANDEMIA EN PERÚ") #Cambiar el nombre de la ventana 
raiz.geometry("500x480") #Configurar tamaño
raiz.resizable(0,0)
npaci = DoubleVar()
time = DoubleVar()

fondo = PhotoImage(file="..\\imagenes\\fondo.gif")
background_label = Label(image=fondo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

Label(raiz, text="Seleccione heuristica de variable: ",
      width=25, anchor="sw").place(x=100, y=150)
CHvar = ttk.Combobox(raiz, state="readonly", width=35,
                     values=["Primera variable",
                             "Variable con el valor mínimo más pequeño",
                             "Variable con el valor máximo más alto"])
CHvar.current(0)
CHvar.place(x=100, y=190)

Label(raiz, text="Seleccione heuristica de valor: ",
      width=25, anchor="sw").place(x=100, y=240)
CHval = ttk.Combobox(raiz, state="readonly", width=35,
                     values=["Menor valor", "Mayor valor",
                             "Valor medio inferior",
                             "Valor medio superior"])
CHval.current(0)
CHval.place(x=100, y=280)

def vdata():
    visualize_data()

def vmap():
    visualize_map()

def vsolution():
    pl,np,t = OrganizePandemic(n_camas_en_hospitales, pacientes_contagio,
                                   pacientes_loc, hospitales_loc,
                                   CHvar.current(), CHval.current())
    npaci.set(np)
    time.set(t)
    if pl != 0: visualize_solution(pl)

Button(raiz, text="Ver datos del problema", command=vdata).place(x = 100, y=50)
Button(raiz, text="Ver mapa con los datos", command=vmap).place(x = 100, y=100)
Button(raiz, text="Ver solución del problema",
       command=vsolution).place(x = 100, y=330)
Label(raiz, text="Numero de pacientes atendidos: ",
      width=25, anchor="sw").place(x=100, y=380)
Label(raiz, text="Tiempo de ejecución: ",
      width=20, anchor="sw").place(x=100, y=410)
ttk.Entry(raiz, textvariable=npaci, width=15).place(x=320, y=380)
ttk.Entry(raiz, textvariable=time, width=15).place(x=320, y=410)

raiz.mainloop()
