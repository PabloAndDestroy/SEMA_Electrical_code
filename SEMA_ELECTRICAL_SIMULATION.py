#Simulación de corriente y voltaje inducido en una bobina toroidal 
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd


Uo = 4*np.pi*(10**(-7))
Ur = 5000
fem = []
fem1 = []

b = int(input("Grosor de la bobina "))


# Intensidad y frecuencia de la corriente que pasa por el cable
frecuencia = float(input("Ingrese la frecuencia angular de la corriente "))
intensidad = float(input("Ingrese la intensidad de la corriente "))


def fem_distancia_centro():
    #Gráfica según un grosor de la sección transversal específico, y un número específico de espiras
    #La distancia al centro varía y gráfica con respecto a esta.
    a=  float(input("Ingrese grosor de la sección transversal de la bobina "))
    N_vueltas = float(input("Ingrese el número de espiras "))

    fem = []
 
    range_c = range(1, 18)
    for c in range_c:
        fem.append((N_vueltas*Uo*Ur*a/(2*np.pi) * np.log((b+c)/c)*frecuencia*intensidad)/1000)  
    x = range_c
    y = fem
 
    plt.plot(x,y,'red', label=f'con {N_vueltas} vueltas')
    
    plt.legend()
    plt.grid()
    plt.title('FEM obtenida según distancia al cable')
    plt.xlabel("Distancia al cable en mm")
    plt.ylabel("FEM")
    plt.show()



def fem_n_espiras():
    #Gráfica según grosor específico de la seccion transversal y la distancia de la linea al toroide
    #El número de vueltas varía y se grafica con respecto al número de espiras
    a=  float(input("Ingrese grosor de la sección transversal de la bobina "))
    c1 = float(input("Distancia del centro del alambre al toroide "))
   
    fem =[]

    range_N = range(20, 200)
    for N1 in range_N:
        fem.append((N1*Uo*Ur*a/(2*np.pi) * np.log((b+c1)/c1)*frecuencia*intensidad)/1000) 
        
    x1 = range_N
    y1 = fem1
   
    plt.plot(x1,y1, 'purple', label=f'Con {c1} mm de distancia al cable')
    
    plt.legend()
    plt.grid()
    plt.title('FEM obtenida número de espiras')
    plt.xlabel("Numero de espiras ")
    plt.ylabel("FEM")
    plt.show()

def fem_parametro_a():
    #Gráfica con número de espiras especificado y distancia de la linea al cable
    #Se varía el grosor de la sección transversal de la bobina y se grafica con respecto a este
    range_A = range(5, 20)
    N = int(input("Número de vueltas "))
    c = float(input("Ingrese distancia al cable de la bobina "))
    for a in range_A:
        fem.append((N*Uo*Ur*a/(2*np.pi) * np.log((b+c)/c)*frecuencia*intensidad)/1000)
    x = range_A
    y = fem
    plt.plot(x,y, 'green')
    plt.grid()
    plt.title('FEM obtenida según grosor de la sección transversal')
    plt.xlabel("Grosor sección transversal en mm")
    plt.ylabel("FEM")
    plt.show()




print("1 para Cálcular en función de distancia al cable ")
print("2 para Cácular en función de número de espiras ")
print("3 para Cácular en función del grosor de la sección transversal ")
seleccion = int(input("Ingrese un número "))
if seleccion==1:
    fem_distancia_centro()
    
if seleccion==2:
    fem_n_espiras()
if seleccion==3:
    fem_parametro_a()
