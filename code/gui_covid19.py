from tkinter import *
from tkinter import ttk
from data_visualize import *
from CPmodel import *

raiz = Tk() 
raiz.title("COVID-19 PANDEMIA EN PERÚ") #Cambiar el nombre de la ventana 
raiz.geometry("500x500") #Configurar tamaño
raiz.resizable(0,0)
npaci = DoubleVar()
time = DoubleVar()
pl = 0

fondo = PhotoImage(file="..\\imagenes\\fondo.gif")
background_label = Label(image=fondo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

Label(raiz, text="Seleccione heuristica de variable: ",
      width=25, anchor="sw").place(x=100, y=170)
CHvar = ttk.Combobox(raiz, state="readonly", width=35,
                     values=["Primera variable",
                             "Variable con el valor mínimo más pequeño",
                             "Variable con el valor máximo más alto"])
CHvar.current(0)
CHvar.place(x=100, y=210)

Label(raiz, text="Seleccione heuristica de valor: ",
      width=25, anchor="sw").place(x=100, y=260)
CHval = ttk.Combobox(raiz, state="readonly", width=35,
                     values=["Menor valor", "Mayor valor",
                             "Valor medio inferior",
                             "Valor medio superior"])
CHval.current(0)
CHval.place(x=100, y=300)

Label(raiz, text="Seleccione el caso a probar: ",
      width=23, anchor="sw").place(x=100, y=30)
Casos = ttk.Combobox(raiz, state="readonly", width=38,
                     values=["Todos los pacientes, pero solo camas UCI",
                             "401 pacientes, pero todas las camas"])
Casos.current(0)
Casos.place(x=100, y=70)

def vdata():
    nh, pc, plo = asignar_datos(Casos.current())
    visualize_data(pc, plo, hospitales_loc)

def vmap():
    visualize_map()

def vsolution():
    nh, pc, plo = asignar_datos(Casos.current())
    pl,np,t = OrganizePandemic(nh, pc, plo,hospitales_loc,CHvar.current(), CHval.current())
    npaci.set(np)
    time.set(t)
    if pl != 0:
        visualiza_solumap(pl)
        visualize_solution(pc, plo, hospitales_loc, pl)

Button(raiz, text="Ver datos del problema", command=vdata).place(x = 100, y=120)
Button(raiz, text="Ver mapa con los datos", command=vmap).place(x = 270, y=120)
Button(raiz, text="Ver solución del problema",
       command=vsolution).place(x = 100, y=350)
Label(raiz, text="Numero de pacientes atendidos: ",
      width=25, anchor="sw").place(x=100, y=400)
Label(raiz, text="Tiempo de ejecución: ",
      width=20, anchor="sw").place(x=100, y=430)
ttk.Entry(raiz, textvariable=npaci, width=15).place(x=320, y=400)
ttk.Entry(raiz, textvariable=time, width=15).place(x=320, y=430)

raiz.mainloop()
