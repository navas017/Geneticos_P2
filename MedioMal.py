import random
import numpy as np
import requests

n_rotores = 10
n_individuos = 100
n_generaciones = 1000
c = 0.82
factor = 10

""" Clase que define la combinación de los motores ,varianzas y su valor de adecuación """


class Motores:
    def __init__(self, motor, varianzas, fitness_value):
        self.motor = motor
        self.varianzas = varianzas
        self.fitness_value = fitness_value


""" Bucle para inicializar la pobalción """
poblacion = []
vec_mejora = []
for i in range(n_individuos):
    vars = []
    mots = []
    for j in range(n_rotores):
        var = random.uniform(100, 200)
        vars.append(var)
        #normal = np.random.normal(0, var)
        normal = 0
        mots.append(normal)
    llamada = "http://memento.evannai.inf.uc3m.es/age/robot10?c1=" + str(mots[0]) + "&c2=" + str(
        mots[1]) + "&c3=" + str(mots[2]) + "&c4=" + str(mots[3]) + "&c5=" + str(mots[4]) + "&c6=" + str(
        mots[5]) + "&c7=" + str(mots[6]) + "&c8=" + str(mots[7]) + "&c9=" + str(mots[8]) + "&c10=" + str(mots[9])
    r = requests.get(llamada)
    poblacion.append(Motores(mots, vars, float(r.text)))

""" Bucle para las generaciones """
cont = 0
min_fitness = 10000
minimos = []
while cont < n_generaciones:
    for i in range(len(poblacion)):
        hijo = []
        for j in range(n_rotores):
            suma = poblacion[i].motor[j] + np.random.normal(0, poblacion[i].varianzas[j])
            hijo.append(suma)
        fit_hijo = "http://memento.evannai.inf.uc3m.es/age/robot10?c1=" + str(hijo[0]) + "&c2=" + str(
            hijo[1]) + "&c3=" + str(hijo[2]) + "&c4=" + str(hijo[3]) + "&c5=" + str(hijo[4]) + "&c6=" + str(
            hijo[5]) + "&c7=" + str(hijo[6]) + "&c8=" + str(hijo[7]) + "&c9=" + str(hijo[8]) + "&c10=" + str(hijo[9])
        r = requests.get(fit_hijo)

        if float(r.text) < poblacion[i].fitness_value:          # El hijo es mejor que el padre
            poblacion[i].fitness_value = float(r.text)
            poblacion[i].motor = hijo
            vec_mejora.append(1)
        else:
            vec_mejora.append(0)

        if float(poblacion[i].fitness_value) < min_fitness:
            min_fitness = poblacion[i].fitness_value


    """ Regla de 1/5 """
    if len(vec_mejora) == factor:
        sumatorio = 0
        for valor in vec_mejora:
            sumatorio += valor
        mejora = sumatorio / factor

        if mejora < 0.2:
            for individuo in range(len(poblacion)):
                for k in range(n_rotores):
                    # print("Antes ",poblacion[j].varianzas[k])
                    poblacion[j].varianzas[k] = poblacion[j].varianzas[k] * c
                    # print("Despues ",poblacion[j].varianzas[k])
        if mejora > 0.2:
            for j in range(len(poblacion)):
                for k in range(n_rotores):
                    # print("Antes ",poblacion[j].varianzas[k])
                    poblacion[j].varianzas[k] = poblacion[j].varianzas[k] / c
                    # print("Despues ",poblacion[j].varianzas[k])








    if (len(vec_mejora) > 0) and (len(vec_mejora) % factor == 0):
        aux = []
        if len(vec_mejora) == factor:
            aux = vec_mejora
        else:
            aux = vec_mejora[-factor:]

        sumatorio = 0
        for i in aux:
            sumatorio += i
        mejora = sumatorio / factor

        if mejora < 0.2:
            for j in range(len(poblacion)):
                for k in range(n_rotores):
                    # print("Antes ",poblacion[j].varianzas[k])
                    poblacion[j].varianzas[k] = poblacion[j].varianzas[k] * c
                    # print("Despues ",poblacion[j].varianzas[k])
        if mejora > 0.2:
            for j in range(len(poblacion)):
                for k in range(n_rotores):
                    # print("Antes ",poblacion[j].varianzas[k])
                    poblacion[j].varianzas[k] = poblacion[j].varianzas[k] / c
                    # print("Despues ",poblacion[j].varianzas[k])

    print(min_fitness)
    print(cont)
    cont += 1

"""
for i in range(len(poblacion)):
    print(poblacion[i].motor)
    print(poblacion[i].varianzas)
    print(poblacion[i].fitness_value)
"""
