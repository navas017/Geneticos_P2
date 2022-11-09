import random
import numpy as np
import requests

n_rotores = 4
n_individuos = 100
n_generaciones = 1000
vec_mejora = []
c = 0.82

""" Clase que define la combinación de los motores ,varianzas y su valor de adecuación """
class Motores:
    def __init__(self ,motor ,varianzas ,fitness_value):
        self.motor = motor
        self.varianzas = varianzas
        self.fitness_value = fitness_value

""" Bucle para inicializar la pobalción """
poblacion = []
for i in range(n_individuos):
    vars = []
    mots = []
    for j in range(n_rotores):
        var = random.uniform(0,60)
        vars.append(var)
        normal = np.random.normal(0, var)
        mots.append(normal)
    llamada = "http://memento.evannai.inf.uc3m.es/age/robot4?c1=" + str(mots[0]) + "&c2=" + str(mots[1]) + "&c3=" + str(mots[2]) + "&c4=" + str(mots[3])
    r = requests.get(llamada)
    poblacion.append(Motores(mots,vars,float(r.text)))

""" Creación de los hijos """
cont = 0
while cont < n_individuos:
    hijos = []
    var_hijo = []
    mot_hijo = []
    padre = poblacion[cont]
    madre = poblacion[cont + 1]
    for i in range(n_rotores):
        var_hijo.append((padre.varianzas[i]**2 + madre.varianzas[i]**2)**1/2)
        mot_hijo.append(np.random.normal(0,var_hijo[i]))
        #mot_hijo.append(((padre.motor[i]+madre.motor[i])/2) + (np.random.normal(0,var_hijo[i])))
        llamada2 = "http://memento.evannai.inf.uc3m.es/age/robot4?c1=" + str(mot_hijo[0]) + "&c2=" + str(mot_hijo[1]) + "&c3=" + str(mot_hijo[2]) + "&c4=" + str(mot_hijo[3])
        fit_hijo = requests.get(llamada2)
    poblacion.append(Motores(mot_hijo,var_hijo,float(fit_hijo)))
    cont += 2