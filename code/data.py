import random

n_hospitales = 1 #10 hospitales
n_pacientes = 1000 #1000 pacientes
n_camas_en_hospitales = [25,160,25,62,89,25,25,89,53,62] #numero de camas
n_camas_total = sum(n_camas_en_hospitales)

#Localizacion Pacientes
pacientes_loc = [(0, 0) for _ in range(n_pacientes)]
#Magdalena: 130 (13%) (0-130)
for i in range(43):
    pacientes_loc[i] = (random.uniform(-77.077408,-77.064233),
                        random.uniform(-12.094760,-12.086703))
for i in range(43, 86):
    pacientes_loc[i] = (random.uniform(-77.074011,-77.057703),
                        random.uniform(-12.097704,-12.090738))
for i in range(86, 130):
    pacientes_loc[i] = (random.uniform(-77.077804,-77.061104),
                        random.uniform(-12.093811,-12.088220))
#San Isidro: 340 (34%) (130-470)
for i in range(130, 243):
    pacientes_loc[i] = (random.uniform(-77.059696,-77.012752),
                        random.uniform(-12.100708,-12.090402))
for i in range(243, 356):
    pacientes_loc[i] = (random.uniform(-77.058650,-77.035234),
                        random.uniform(-12.106394,-12.102754))
for i in range(356, 470):
    pacientes_loc[i] = (random.uniform(-77.056745,-77.032664),
                        random.uniform(-12.107044,-12.091744))
#Miraflores: 360 (36%) (470-830)
for i in range(470, 560):
    pacientes_loc[i] = (random.uniform(-77.034170,-77.008764),
                        random.uniform(-12.130429,-12.119353))
for i in range(560, 650):
    pacientes_loc[i] = (random.uniform(-77.039921,-77.027647),
                        random.uniform(-12.124346,-12.109030))
for i in range(650, 740):
    pacientes_loc[i] = (random.uniform(-77.032583,-77.028334),
                        random.uniform(-12.131898,-12.103534))
for i in range(740, 830):
    pacientes_loc[i] = (random.uniform(-77.049920,-77.027175),
                        random.uniform(-12.115954,-12.110751))
#Surquillo: 170 (17%) (830-1000)
for i in range(830, 872):
    pacientes_loc[i] = (random.uniform(-77.025110,-77.017214),
                        random.uniform(-12.118932,-12.102400))
for i in range(872, 914):
    pacientes_loc[i] = (random.uniform(-77.016877,-77.011120),
                        random.uniform(-12.116809,-12.107603))
for i in range(914, 957):
    pacientes_loc[i] = (random.uniform(-77.006433,-76.995997),
                        random.uniform(-12.120664,-12.111664))
for i in range(957, 1000):
    pacientes_loc[i] = (random.uniform(-77.003931,-77.000155),
                        random.uniform(-12.124471,-12.112051))

#Localizacion Hospitales
hospitales_loc = [(-77.070045,-12.092470), (-77.018283,-12.090713),
                  (-77.055142,-12.106902), (-77.046930,-12.106690),
                  (-77.035280,-12.101090), (-77.055142,-12.106902),
                  (-77.017737,-12.128109), (-77.029993,-12.103803),
                  (-77.033510,-12.115010), (-77.033820,-12.125120)]

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
