import random
import numpy as np
import requests

n_rotores = 10
n_generaciones = 1000
c = 0.82
s = 10
inicial =10
final = 110

class Motores:
    def __init__(self, motor, varianzas, fitness_value):
        self.motor = motor
        self.varianzas = varianzas
        self.fitness_value = fitness_value

vec_mejora = []

for generacion in range(n_generaciones):

    if generacion == 0:       # Inicialización del padre
        vars = []
        mots = []
        for rotor in range(n_rotores):
            var = random.uniform(inicial, final)
            vars.append(var)
            #normal = np.random.normal(0, var)
            normal = 0
            mots.append(normal)
        fit_padre = "http://memento.evannai.inf.uc3m.es/age/robot10?c1=" + str(mots[0]) + "&c2=" + str(
            mots[1]) + "&c3=" + str(mots[2]) + "&c4=" + str(mots[3]) + "&c5=" + str(mots[4]) + "&c6=" + str(
            mots[5]) + "&c7=" + str(mots[6]) + "&c8=" + str(mots[7]) + "&c9=" + str(mots[8]) + "&c10=" + str(mots[9])
        fitness_padre = requests.get(fit_padre)
        padre = Motores(mots, vars, float(fitness_padre.text))

    """ Creación del hijo """
    motor_hijo = []
    varianzas_hijo = []
    for rotor in range(n_rotores):
        motor_hijo.append((padre.motor[rotor] + np.random.normal(0,padre.varianzas[rotor])))
        varianzas_hijo.append(padre.varianzas[rotor])
    fit_hijo = "http://memento.evannai.inf.uc3m.es/age/robot10?c1=" + str(motor_hijo[0]) + "&c2=" + str(
        motor_hijo[1]) + "&c3=" + str(motor_hijo[2]) + "&c4=" + str(motor_hijo[3]) + "&c5=" + str(
        motor_hijo[4]) + "&c6=" + str(motor_hijo[5]) + "&c7=" + str(motor_hijo[6]) + "&c8=" + str(
        motor_hijo[7]) + "&c9=" + str(motor_hijo[8]) + "&c10=" + str(motor_hijo[9])
    fitness_hijo = requests.get(fit_hijo)
    hijo = Motores(motor_hijo, varianzas_hijo, float(fitness_hijo.text))

    print(padre.fitness_value)
    print(hijo.fitness_value)

    if hijo.fitness_value < padre.fitness_value:
        print("Entra")
        padre.varianzas = hijo.varianzas
        padre.motor = hijo.motor
        padre.fitness_value = hijo.fitness_value
        vec_mejora.append(1)
    else:
        vec_mejora.append(0)

    if len(vec_mejora) % s == 0:
        aux = []
        if len(vec_mejora) == s:
            aux = vec_mejora
        else:
            aux = vec_mejora[-s:]

        sumatorio = 0
        for elemento in aux:
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

    print("Iteracion: ", generacion)
    print("Fitness: ", padre.fitness_value)




