from ortools.sat.python import cp_model # CP-SAT solver

def dist(p1,p2):
  return int(((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5)

def maxdist(pacientes_loc, hospitales_loc):
    max_dist = 0
    for i in range(len(hospitales_loc)):
        for k in range(len(pacientes_loc)):
            d = dist(pacientes_loc[k],hospitales_loc[i])
            if max_dist < d:
                max_dist = d
    return max_dist

def OrganizePandemic(n_camas_en_hospitales, pacientes_contagio, pacientes_loc, hospitales_loc, heuvar, heuval):
    model = cp_model.CpModel()
    
    # variables y dominios
    x = {} #diccionarios en python
    for i in range(len(hospitales_loc)):
        for j in range(n_camas_en_hospitales[i]):
            for k in range(len(pacientes_loc)):
                x[(i,j,k)] = model.NewBoolVar("x_" + str(i) + "_" + str(j) + "_" + str(k))

    #optimización
    max_dist = maxdist(pacientes_loc, hospitales_loc)
    l = []
    for i in range(len(hospitales_loc)):
        for j in range(n_camas_en_hospitales[i]):
            for k in range(len(pacientes_loc)):
                l += [(100 + int(100 * pacientes_contagio[k] / 5) - int(100 * dist(pacientes_loc[k],hospitales_loc[i]) / max_dist)) * x[(i,j,k)]]
    model.Maximize(sum(l))
    
    #constraints
    for i in range(len(hospitales_loc)):
        for j in range(n_camas_en_hospitales[i]):
            model.Add(sum([x[(i,j,k)] for k in range(len(pacientes_loc))]) <= 1)
    for k in range(len(pacientes_loc)):
        n_paciente_en_camas_hospitales = []
        for i in range(len(hospitales_loc)):
            n_paciente_en_camas_hospitales += [sum([x[(i,j,k)] for j in range(n_camas_en_hospitales[i])])]
        model.Add(sum(n_paciente_en_camas_hospitales) <= 1)

    #heuristicas
    for i in range(len(hospitales_loc)):
        for j in range(n_camas_en_hospitales[i]):
            pacientes = []
            for k in range(len(pacientes_loc)):
              pacientes += [x[(i,j,k)]]
            model.AddDecisionStrategy(pacientes, heuvar, heuval)

    #solver
    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    if status == cp_model.OPTIMAL:
        print("N pacientes atendidos:",solver.ObjectiveValue())
        print("Tiempo:",solver.WallTime())
        plot_lineas = [[] for _ in range(len(hospitales_loc))]
        for i in range(len(hospitales_loc)):
            for j in range(n_camas_en_hospitales[i]):
                for k in range(len(pacientes_loc)):
                    if solver.Value(x[(i,j,k)]) == 1:
                        linea_abcisa = [hospitales_loc[i][0], pacientes_loc[k][0]]
                        linea_ordenada = [hospitales_loc[i][1], pacientes_loc[k][1]]
                        plot_lineas[i].append([linea_abcisa, linea_ordenada])
        return plot_lineas
    return 0
    
        






  

