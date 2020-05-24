from tkinter import *
from datos_visualize import *
from CPmodel import *

raiz = Tk() 
raiz.title("COVID-19 PANDEMIA EN PERÚ") #Cambiar el nombre de la ventana 
raiz.geometry("520x480") #Configurar tamaño  
raiz.config(bg="green") #Cambiar color de fondo
raiz.resizable(0,0)

def vdata():
    visualize_data()

def vsolution():
    plot_lineas = OrganizePandemic(n_camas_en_hospitales, pacientes_contagio,
                                   pacientes_loc, hospitales_loc)
    if plot_lineas != 0: visualize_solution(plot_lineas)

Button(raiz, text="Ver datos del problema",
       command=vdata).place(x = 190, y=150)

Button(raiz, text="Ver solución del problema",
       command=vsolution).place(x = 180, y=300)

raiz.mainloop()
