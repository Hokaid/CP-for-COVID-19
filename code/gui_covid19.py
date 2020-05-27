from tkinter import *
from tkinter import ttk
from data import *
from CPmodel import *
from visualize import *

raiz = Tk() 
raiz.title("COVID-19 PANDEMIA EN PERÚ") #Cambiar el nombre de la ventana 
raiz.geometry("520x480") #Configurar tamaño
raiz.resizable(0,0)

fondo = PhotoImage(file="..\\imagenes\\fondo.gif")
background_label = Label(image=fondo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

Label(raiz, text="Seleccione heuristica de variable: ",
      width=25, anchor="sw").place(x=100, y=130)
CHvar = ttk.Combobox(raiz, state="readonly", width=35,
                     values=["Primera variable",
                             "Variable con el valor mínimo más pequeño",
                             "Variable con el valor máximo más alto"])
CHvar.current(0)
CHvar.place(x=100, y=170)

Label(raiz, text="Seleccione heuristica de valor: ",
      width=25, anchor="sw").place(x=100, y=220)
CHval = ttk.Combobox(raiz, state="readonly", width=35,
                     values=["Menor valor", "Mayor valor",
                             "Valor medio inferior",
                             "Valor medio superior"])
CHval.current(0)
CHval.place(x=100, y=260)

def vdata():
    visualize_data(pacientes_contagio, pacientes_loc, hospitales_loc)

def vsolution():
    plot_lineas = OrganizePandemic(n_camas_en_hospitales, pacientes_contagio,
                                   pacientes_loc, hospitales_loc,
                                   CHvar.current(), CHval.current())
    if plot_lineas != 0: visualize_solution(plot_lineas, pacientes_contagio,
                                            pacientes_loc, hospitales_loc)

Button(raiz, text="Ver datos del problema",
          command=vdata).place(x = 100, y=70)
Button(raiz, text="Ver solución del problema",
          command=vsolution).place(x = 100, y=310)

raiz.mainloop()
