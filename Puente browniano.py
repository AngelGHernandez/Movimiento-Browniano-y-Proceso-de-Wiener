# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 01:51:56 2023

@author: AngelG
"""
# Importar librerías
import random
import matplotlib.pyplot as pyplot

# Declarar arreglos
brownianMotion = []
brownianMotion_1 = []
brownianMotion_2 = []

# Declarar variables        
tiempo = 200
dist = 10
pos = 0
pos_1 = 0
pos_2 = 0
# Simulación
#El punto de inicio y el nivel final se denominan "condiciones de borde", y el punto medio en el que la trayectoria cruza el nivel final se denomina "punto de cruce".

#particula roja
for n in range(tiempo):
    rand = random.randint(0,1)
    if rand == 0:
        pos = pos+dist
    else:
        pos = pos-dist
    brownianMotion.append(pos)

#particula verde
for n in range(tiempo):
    rand = random.randint(0,1)
    if rand == 0:
        pos_1 = pos_1+dist
    else:
        pos_1 = pos_1-dist
    brownianMotion_1.append(pos_1)


#particula azul
for n in range(tiempo):
    rand = random.randint(0,1)
    if rand == 0:
        pos_2 = pos_2+dist
    else:
        pos_2 = pos_2-dist
    brownianMotion_2.append(pos_2)

# Etiquetas
pyplot.title("Puente Browniano")
pyplot.xlabel("Pasos")
pyplot.ylabel("Posición")

# Grafica
# Cada corrida presenta una grafica diferente para las diferentes "particulas" con distintas condiciones de borde
pyplot.plot(brownianMotion)
pyplot.plot(brownianMotion_1)
pyplot.plot(brownianMotion_2)

pyplot.show()
