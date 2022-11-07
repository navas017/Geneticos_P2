import random
import numpy as np
import requests

n_rotores = 4
n_individuos = 100
vec_mejora = []
varianzas = []
motores = []

individuo = 0
while individuo < n_individuos:
    rotor = 0
    while rotor < n_rotores:
        var = random.uniform(0,60)
        varianzas.append(var)
        normal = np.random.normal(0,var)
        motores.append(normal)
    llamada = "http://memento.evannai.inf.uc3m.es/age/robot4?c1=" + str(motores[0]) + "&c2=" + str(motores[1]) + "&c3=" + str(motores[2]) + "&c4=" + str(motores[3])

#llamada

r = requests.get(llamada)
print(r.text)