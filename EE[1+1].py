import random
import numpy as np
import requests

n_rotores = 4
n_generaciones = 100000
c = 0.82
s = 10
inicial = 100
final = 180

class Motores:
    def __init__(self, motor, varianzas, fitness_value):
        self.motor = motor
        self.varianzas = varianzas
        self.fitness_value = fitness_value

vec_mejora = []

for generacion in range(n_generaciones):

    if generacion == 0:       # Inicialización del padre, con varianzas aleatorias, motores en 0 y valor fitness
        vars = []
        mots = []
        for rotor in range(n_rotores):
            var = random.uniform(inicial, final)
            vars.append(var)
            #normal = np.random.normal(0, var)
            normal = 0
            mots.append(normal)
        fit_padre = "http://memento.evannai.inf.uc3m.es/age/robot4?c1=" + str(mots[0]) + "&c2=" + str(mots[1]) + "&c3=" + str(mots[2]) + "&c4=" + str(mots[3])
        fitness_padre = requests.get(fit_padre)
        padre = Motores(mots, vars, float(fitness_padre.text))

    """ Creación del hijo """
    motor_hijo = []
    varianzas_hijo = []
    for rotor in range(n_rotores):
        motor_hijo.append((padre.motor[rotor] + np.random.normal(0,padre.varianzas[rotor])))
        varianzas_hijo.append(padre.varianzas[rotor])
    fit_hijo = "http://memento.evannai.inf.uc3m.es/age/robot4?c1=" + str(motor_hijo[0]) + "&c2=" + str(motor_hijo[1]) + "&c3=" + str(motor_hijo[2]) + "&c4=" + str(motor_hijo[3])
    fitness_hijo = requests.get(fit_hijo)
    hijo = Motores(motor_hijo, varianzas_hijo, float(fitness_hijo.text))


    if (hijo.fitness_value < padre.fitness_value):
        padre.varianzas = hijo.varianzas
        padre.motor = hijo.motor
        padre.fitness_value = hijo.fitness_value
        vec_mejora.append(1)
    else:
        vec_mejora.append(0)

    if len(vec_mejora) == s:

        sumatorio = 0
        for elemento in vec_mejora:
            sumatorio += elemento
        media = sumatorio / s

        if media < 0.2:
            for rotor in range(n_rotores):
                # print("Antes ",poblacion[j].varianzas[k])
                padre.varianzas[rotor] = padre.varianzas[rotor] * c
                # print("Despues ",poblacion[j].varianzas[k])
        if media > 0.2:
            for rotor in range(n_rotores):
                # print("Antes ",poblacion[j].varianzas[k])
                padre.varianzas[rotor] = padre.varianzas[rotor] / c
                # print("Despues ",poblacion[j].varianzas[k])
        vec_mejora = []


    print("Iteracion: ", generacion)
    print("Fitness: ", padre.fitness_value)




