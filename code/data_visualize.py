import random
import gmplot 
from csv import reader
import matplotlib.pyplot as plt # Data visualization
plt.rcParams["figure.figsize"] = (40,15)
from itertools import cycle
import webbrowser
from sklearn.model_selection import train_test_split

def cargarCSV(csv, cols):
    data = [[] for _ in range(len(cols))]
    resultado = []
    with open(csv, 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_of_rows = list(csv_reader)
    for item in list_of_rows:
        for i in range(len(cols)):
            data[i].append(float(item[cols[i]]))
    for i in range(len(cols)):
        resultado.append(data[i])
    return resultado

miraflores = cargarCSV('..\csv files\Miraflores.csv', [1,3])
sanIsidro = cargarCSV('..\csv files\SanIsidro.csv', [1,3])
surquillo = cargarCSV('..\csv files\Surquillo.csv', [1,3])
magdalena = cargarCSV('..\csv files\Magdalena.csv', [1,3])
hospitales = cargarCSV('..\csv files\Hospitales+Camas.txt', [2,3,5,4])
contagio = cargarCSV('..\csv files\severidad.txt',[0])
p = []
p.append(miraflores)
p.append(sanIsidro)
p.append(surquillo)
p.append(magdalena)

n_pacientes = 0
pacientes_loc = []
n_camas_en_hospitales = []
pacientes_contagio = []

pacientes = [[],[]] #Localizacion Pacientes
for distrito in p:
    for i in range(len(distrito[0])):
        pacientes[0].append((distrito[0][i]*100, distrito[1][i]*100))
for sev in contagio[0]:
    pacientes[1].append(sev)
h = [] #Localizacion Hospitales
for i in range(len(hospitales[0])):
    h.append((hospitales[0][i]*100, hospitales[1][i]*100))
n_hospitales = len(h) #Numero de hospitales
hospitales_loc = h
camasuci = [] #Camas por hospital
camas = []
for i in range(len(hospitales[2])):
    camasuci.append(int(hospitales[3][i]))
    camas.append(int(hospitales[2][i]) + int(hospitales[3][i]))
paciente ,hospitalizar = train_test_split(pacientes[0],test_size=0.1)
paciente, pcontag = train_test_split(pacientes[1],test_size=0.1)

def asignar_datos(case):
    if case == 0:
        n_pacientes = len(pacientes[0]) #Numero de pacientes
        n_camas_en_hospitales = camasuci
        n_camas_total = sum(n_camas_en_hospitales) #Numero de camas en total
        # Localizacion
        pacientes_loc = pacientes[0]
        pacientes_contagio = pacientes[1]
    elif case == 1:
        n_pacientes = len(hospitalizar) #Numero de pacientes
        n_camas_en_hospitales = camas
        n_camas_total = sum(n_camas_en_hospitales) #Numero de camas en total
        # Localizacion
        pacientes_loc = hospitalizar
        pacientes_contagio = pcontag
    return n_camas_en_hospitales, pacientes_contagio, pacientes_loc

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

def visualize_map():
    gmap = gmplot.GoogleMapPlotter(-12.1103929, -77.0347696, 14)    
    gmap.scatter( hospitales[0], hospitales[1], '#000080', size = 100, marker = False ) 
    gmap.scatter( miraflores[0], miraflores[1], '#FF3333', size = 20, marker = False ) 
    gmap.scatter( sanIsidro[0], sanIsidro[1], '#006633', size = 20, marker = False ) 
    gmap.scatter( surquillo[0], surquillo[1], '#CC0066', size = 20, marker = False ) 
    gmap.scatter( magdalena[0], magdalena[1], '#999900', size = 20, marker = False ) 
    gmap.apikey = "AIzaSyA_2cjPy9AbF1aU1pa1oOo7_JmezBCy01c"
    gmap.draw( "map13.html" )
    webbrowser.open("map13.html",new=2)

def visualiza_solumap(resultado):
    gmap = gmplot.GoogleMapPlotter(-12.1103929, -77.0347696, 14)    
    gmap.scatter( hospitales[0], hospitales[1], '#000080', size = 100, marker = False ) 
    gmap.scatter( miraflores[0], miraflores[1], '#FF3333', size = 20, marker = False ) 
    gmap.scatter( sanIsidro[0], sanIsidro[1], '#006633', size = 20, marker = False ) 
    gmap.scatter( surquillo[0], surquillo[1], '#CC0066', size = 20, marker = False ) 
    gmap.scatter( magdalena[0], magdalena[1], '#999900', size = 20, marker = False ) 
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
