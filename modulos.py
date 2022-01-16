import numpy as np
from scipy.optimize import root

def solicitar_requerimientos(requirements):
    datos_exportados=[]
    #Recorre la lista de requerimientos para una función
    for n in requirements:
        datum=float(input(f"Por favor introduzca el {n} ")) 
        datos_exportados.append(datum)
    return datos_exportados

def calcular_masa_total_minima_launch(check):
    #Datos Default
    # mu = 0.172 #Coeficiente de masa total
    # e = 0.08 #Coeficiente de masa estructural
    # delta_v = 7000.0 #Delta v requerido (m/s)
    # m_c = 500.0 #Masa de carga (kg)
    # I_sp = 311.0 #Impulso especifico (s)
    # g0 = 9.81 #Aceleracion gravitacional en la superficie terrestre (m/s^2)
    # m_p = 321.21 #Flujo masico (kg/s)
    
    if check ==1: #Caso de usar datos propios
        requerimientos=["Coeficiente de Masa Total (μ)",
        "Coeficiente de Masa estructural(e)",
        "ΔV",
        "Payload(Masa de carga)",
        "Impulso Específico",
        "Aceleración Gravitacional (m/s^2)",
        "Flujo Másico (kg/s)"
        ]
        datos_solicitados=solicitar_requerimientos(requerimientos)
        datos_necesarios = {
        "mu":datos_solicitados[0],
        "e":datos_solicitados[1],
        "delta_v":datos_solicitados[2],
        "m_c":datos_solicitados[3],
        "I_sp":datos_solicitados[4],
        "g0":datos_solicitados[5],
        "m_p":datos_solicitados[6]
        }
    
    elif check ==2: #Caso de usar los datos default
        datos_necesarios = {
        "mu": 0.172,
        "e":0.08,
        "delta_v":7000,
        "m_c":500,
        "I_sp":311,
        "g0":9.81,
        "m_p":321.21
        }
    def funcion_optimizable(x): #Definicion de la funcion que se va a optimizar.
        f = datos_necesarios["g0"]*datos_necesarios["I_sp"]*np.log(x/(datos_necesarios["e"]*(x-datos_necesarios["m_c"])+datos_necesarios["m_c"]))-(datos_necesarios["g0"]*x*(1-datos_necesarios["mu"])/datos_necesarios["m_p"])-datos_necesarios["delta_v"]
        return f

    m_0 = root(fun=funcion_optimizable,x0=10000) #Se usa un estimado inicial de m_0 = 10000 kg.
    return m_0.x[0]#Se retorna el valor de interés

