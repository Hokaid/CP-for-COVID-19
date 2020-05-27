import random
import gmplot 
from csv import reader
import matplotlib.pyplot as plt # Data visualization
plt.rcParams["figure.figsize"] = (40,15)
from itertools import cycle

n_hospitales = 10 #10 hospitales
n_camas_en_hospitales = [25,160,25,62,89,25,25,89,53,62] #numero de camas
n_camas_total = sum(n_camas_en_hospitales)

def cargarCSV(csv):
    latitude_list = []
    longitude_list = []
    cordenadas = []
    with open(csv, 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Pass reader object to list() to get a list of lists
        list_of_rows = list(csv_reader)
        #print(list_of_rows)
    for item in list_of_rows:
        latitude_list.append(float(item[1]))
        longitude_list.append(float(item[3]))
    cordenadas.append(latitude_list)
    cordenadas.append(longitude_list)
    return cordenadas

miraflores = cargarCSV('..\csv files\Miraflores.csv')
sanIsidro = cargarCSV('..\csv files\SanIsidro.csv')
surquillo = cargarCSV('..\csv files\Surquillo.csv')
magdalena = cargarCSV('..\csv files\Magdalena.csv')

#Localizacion Pacientes
n_pacientes = len(miraflores[0])+len(sanIsidro[0])+len(surquillo[0])+len(magdalena[0])
cantpaci = 0
pacientes_loc = [(0, 0) for _ in range(n_pacientes)]
for i in range(len(miraflores[0])):
    pacientes_loc[i] = (miraflores[1][i], miraflores[0][i])
cantpaci = len(miraflores[0])
for i in range(cantpaci, cantpaci+len(sanIsidro[0])):
    pacientes_loc[i] = (sanIsidro[1][i-cantpaci], sanIsidro[0][i-cantpaci])
cantpaci = cantpaci+len(sanIsidro[0])
for i in range(cantpaci, cantpaci+len(surquillo[0])):
    pacientes_loc[i] = (surquillo[1][i-cantpaci], surquillo[0][i-cantpaci])
cantpaci = cantpaci+len(surquillo[0])
for i in range(cantpaci, n_pacientes):
    pacientes_loc[i] = (magdalena[1][i-cantpaci], magdalena[0][i-cantpaci])

#Localizacion Hospitales
hospitales_loc = [(-77.070045,-12.092470), (-77.018283,-12.090713),
                  (-77.055142,-12.106902), (-77.046930,-12.106690),
                  (-77.035280,-12.101090), (-77.055142,-12.106902),
                  (-77.017737,-12.128109), (-77.029993,-12.103803),
                  (-77.033510,-12.115010), (-77.033820,-12.125120)]
hospitales = [[0]*n_hospitales,[0]*n_hospitales]
for i in range(len(hospitales_loc)):
    hospitales[1][i], hospitales[0][i] = hospitales_loc[i]

#grado de contagio
pacientes_contagio = [0 for _ in range(n_pacientes)]
for i in range(n_pacientes):
    probgrado = random.random()
    if probgrado <= 0.202: #Asymptomatic 20.2%
        pacientes_contagio[i] = 1
    elif probgrado > 0.202 and probgrado <= 0.549: #Mild 34.7%
        pacientes_contagio[i] = 2
    elif probgrado > 0.549 and probgrado <= 0.801: #Strong 25.2%
        pacientes_contagio[i] = 3
    elif probgrado > 0.801 and probgrado <= 0.939: #Hospitalization 13.8%
        pacientes_contagio[i] = 4
    elif probgrado > 0.939: #UCI 6.1%
        pacientes_contagio[i] = 5

def visualize_data():
    sombra_contagio = [int(sev*255/5) for sev in pacientes_contagio]
    color_contagio = ["#%02x0000" % (sev) for sev in sombra_contagio]
    tamano_contagio = [k**2.5 for k in pacientes_contagio]
    plt.scatter(*zip(*pacientes_loc), s=tamano_contagio, c=color_contagio, label="Patients")
    plt.scatter(*zip(*hospitales_loc), s=1000, c="b", marker="P", label="Hospitals")
    plt.legend()
    plt.axis('off')
    plt.show()

def visualize_solution(plot_lineas):
    sombra_contagio = [int(sev*255/5) for sev in pacientes_contagio]
    color_contagio = ["#%02x0000" % (sev) for sev in sombra_contagio]
    tamano_contagio = [k**2.5 for k in pacientes_contagio]
    plt.scatter(*zip(*pacientes_loc), s=tamano_contagio, c=color_contagio, label="Pacientes", zorder=2)
    plt.scatter(*zip(*hospitales_loc), s=1000, c="b", marker="P", label="Hospitales", zorder=3)
    colores = cycle('bgrcmk')
    for i in range(len(hospitales_loc)):
        c = next(colores)
        for (x_, y_) in plot_lineas[i]:
            plt.plot(x_, y_, c=c, linewidth=0.5, zorder=1)
    plt.legend()
    plt.axis('off')
    plt.show()

def visualize_map():
    gmap = gmplot.GoogleMapPlotter(-12.1103929, -77.0347696, 14)
    gmap.scatter( hospitales[0], hospitales[1], '#0000FF', size = 100, marker = False )
    gmap.scatter( miraflores[0], miraflores[1], '#FF3333', size = 20, marker = False )
    gmap.scatter( sanIsidro[0], sanIsidro[1], '#006633', size = 20, marker = False )
    gmap.scatter( surquillo[0], surquillo[1], '#CC0066', size = 20, marker = False )
    gmap.scatter( magdalena[0], magdalena[1], '#999900', size = 20, marker = False )
    gmap.apikey = "AIzaSyA_2cjPy9AbF1aU1pa1oOo7_JmezBCy01c"
    gmap.draw( "map13.html" ) 
