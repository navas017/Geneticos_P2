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
for i in range(n_individuos/2):
    hijos = []
