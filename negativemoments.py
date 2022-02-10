""" Programa para Calcular coeficientes momentos negativos en losas de dos direcciones
ACI-319-2014 para losa caso 2 (Continuidad en todos los lados) """

# Elaborado por JLU

import numpy as np

# To do
# Que el usuario solo introduzca la longitud de ambos lados sin importar el orden (CHECK)
# Introducir los argumentos desde la linea de comandos
# Usar polinomio de grado dos en vez de interpolacion lineal
# Introducir casos restantes

# Caso 2
relacion = [0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1]
ca = [0.086, 0.084, 0.081, 0.077, 0.074,
      0.069, 0.065, 0.06, 0.055, 0.05, 0.045]
cb = [0.006, 0.007, 0.01, 0.014, 0.017,
      0.022, 0.027, 0.031, 0.037, 0.041, 0.045]

lados=[]
lado1 = float(input('Lado uno: '))
lado2 = float(input('Lado dos: '))

lados.append(lado1)
lados.append(lado2)
lados.sort()

if lados[0]/lados[1] < 0.5:
    print('No es una losa de dos direcciones')
else:
    m = lados[0]/lados[1]
    y = np.interp(m, relacion, ca)
    y2 = np.interp(m, relacion, cb)
    print(f"Ca is {y:.5f} and Cb is {y2:.5f}")
