import matplotlib.pyplot as plt # Data visualization
plt.rcParams["figure.figsize"] = (40,15)
from itertools import cycle

def visualize_data(pacientes_contagio, pacientes_loc, hospitales_loc):
    sombra_contagio = [int(sev*255/5) for sev in pacientes_contagio]
    color_contagio = ["#%02x0000" % (sev) for sev in sombra_contagio]
    tamano_contagio = [k**2.5 for k in pacientes_contagio]
    plt.scatter(*zip(*pacientes_loc), s=tamano_contagio, c=color_contagio, label="Patients")
    plt.scatter(*zip(*hospitales_loc), s=1000, c="b", marker="P", label="Hospitals")
    plt.legend()
    plt.axis('off')
    plt.show()

def visualize_solution(plot_lineas, pacientes_contagio, pacientes_loc, hospitales_loc):
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
