import random
import gmplot 
from csv import reader
import matplotlib.pyplot as plt # Data visualization
plt.rcParams["figure.figsize"] = (40,15)
from itertools import cycle
import webbrowser
from sklearn.model_selection import train_test_split

def cargarCSV(csv):
    latitude_list = []
    longitude_list = []
    distrito = []
    with open(csv, 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_of_rows = list(csv_reader)
    for item in list_of_rows:
        latitude_list.append(float(item[1]))
        longitude_list.append(float(item[3]))
    distrito.append(latitude_list)
    distrito.append(longitude_list)
    return distrito

def cargarCSVHospitales(csv):
    latitude_list = []
    longitude_list = []
    numeroCamas = []
    uci = []
    hospital = []
    with open(csv, 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_of_rows = list(csv_reader)
    for item in list_of_rows:
        latitude_list.append(float(item[2]))
        longitude_list.append(float(item[3]))
        numeroCamas.append(int(item[5]))
        uci.append(int(item[4]))
    hospital.append(latitude_list)
    hospital.append(longitude_list)
    hospital.append(numeroCamas)
    hospital.append(uci)
    return hospital

miraflores = cargarCSV('..\csv files\Miraflores.csv')
sanIsidro = cargarCSV('..\csv files\SanIsidro.csv')
surquillo = cargarCSV('..\csv files\Surquillo.csv')
magdalena = cargarCSV('..\csv files\Magdalena.csv')
hospitales = cargarCSVHospitales('..\csv files\Hospitales+Camas.txt')
p = []
p.append(miraflores)
p.append(sanIsidro)
p.append(surquillo)
p.append(magdalena)

n_pacientes = 0
n_hospitales = 0
pacientes_loc = []
hospitales_loc = []
n_camas_en_hospitales = []
pacientes_contagio = []

pacientes = [] #Localizacion Pacientes
for distrito in p:
    for i in range(len(distrito[0])):
        pacientes.append((distrito[0][i]*100, distrito[1][i]*100))
h = [] #Localizacion Hospitales
for i in range(len(hospitales[0])):
    h.append((hospitales[0][i]*100, hospitales[1][i]*100))
n_hospitales = len(h) #Numero de hospitales
hospitales_loc = h

def generar_datos(case):
    camas = [] #Camas por hospital
    for i in range(len(hospitales[2])):
        if case == 0:
            camas.append(hospitales[3][i])
        elif case == 1:
            camas.append(hospitales[2][i] + hospitales[3][i])
    if case == 0:
        hospitalizar = pacientes
    elif case == 1:
        paciente ,hospitalizar = train_test_split(pacientes,test_size=0.1)    
    n_pacientes = len(hospitalizar) #Numero de pacientes
    n_camas_en_hospitales = camas
    n_camas_total = sum(n_camas_en_hospitales) #Numero de camas en total
    # Localizacion
    pacientes_loc = hospitalizar
    print(n_pacientes, n_camas_total)
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
    return n_camas_en_hospitales, pacientes_contagio, pacientes_loc, hospitales_loc

def visualize_data(pacientes_contagio, pacientes_loc, hospitales_loc):
    sombra_contagio = [int(sev*255/5) for sev in pacientes_contagio]
    color_contagio = ["#%02x0000" % (sev) for sev in sombra_contagio]
    tamano_contagio = [k**2.5 for k in pacientes_contagio]
    plt.scatter(*zip(*pacientes_loc), s=tamano_contagio, c=color_contagio, label="Patients")
    plt.scatter(*zip(*hospitales_loc), s=200, c="b", marker="P", label="Hospitals")
    plt.legend()
    plt.axis('off')
    plt.show()

def visualize_solution(pacientes_contagio, pacientes_loc, hospitales_loc, plot_lineas):
    sombra_contagio = [int(sev*255/5) for sev in pacientes_contagio]
    color_contagio = ["#%02x0000" % (sev) for sev in sombra_contagio]
    tamano_contagio = [k**2.5 for k in pacientes_contagio]
    plt.scatter(*zip(*pacientes_loc), s=tamano_contagio, c=color_contagio, label="Pacientes", zorder=2)
    plt.scatter(*zip(*hospitales_loc), s=200, c="b", marker="P", label="Hospitales", zorder=3)
    colores = cycle('bgrcmk')
    for i in range(len(hospitales_loc)):
        c = next(colores)
        for (x_, y_) in plot_lineas[i]:
            plt.plot(x_, y_, c=c, linewidth=0.5, zorder=1)
    plt.legend()
    plt.axis('off')
    plt.show()

def visualize_map(pacientes_loc):
    infectados = [[],[]]
    for i in range(len(pacientes_loc)):
        a,b = pacientes_loc[i]
        infectados[0].append(a/100)
        infectados[1].append(b/100)
    gmap = gmplot.GoogleMapPlotter(-12.1103929, -77.0347696, 14)
    gmap.scatter( infectados[0], infectados[1], '#999900', size = 20, marker = False )
    gmap.scatter( hospitales[0], hospitales[1], '#000000', size = 100, marker = False )
    gmap.apikey = "AIzaSyA_2cjPy9AbF1aU1pa1oOo7_JmezBCy01c"
    gmap.draw( "map13.html" )
    webbrowser.open("map13.html",new=2)

def visualiza_solumap(pacientes_loc, resultado):
    infectados = [[],[]]
    for i in range(len(pacientes_loc)):
        a,b = pacientes_loc[i]
        infectados[0].append(a/100)
        infectados[1].append(b/100)
    gmap = gmplot.GoogleMapPlotter(-12.1103929, -77.0347696, 14)    
    gmap.scatter( hospitales[0], hospitales[1], '#000080', size = 100, marker = False )
    gmap.scatter( infectados[0], infectados[1], '#999900', size = 20, marker = False )
    colores = ['#FF0000','#808000','#FFA07A','#5B2C6F','#5367F4','#B8369F','#1A1362','#A04020','#117A65','#000000']
    for i in range(10):
        for (x_, y_) in resultado[i]:
            x, y = zip(*[
            (x_[0]/100,y_[0]/100),
            (x_[1]/100,y_[1]/100),
            ])
            gmap.plot(x, y, colores[i], edge_width=1)
    gmap.apikey = "AIzaSyA_2cjPy9AbF1aU1pa1oOo7_JmezBCy01c"
    gmap.draw( "map14.html" )
    webbrowser.open("map14.html",new=2)
