import numpy as np
from pandas import period_range
from scipy.optimize import root
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText
from matplotlib import animation

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

def calcular_posiciones_orbit(e,a,nombre):
    """
    Estructura de datos ej:
    resultado = [punto en x, puntos en y, apogeo, perigeo, coodenadas apo, coordenadas peri]
    """
    resultado = [] #
    x=[]
    y=[]
    perio=843840923843290
    apo=0
    coordenadas_apo={"x":0,"y":0}
    coordenadas_perio={"x":0,"y":0}
    coleccion = np.linspace(0,2*3.1415927585,500)
    for cuenta,phi in enumerate(coleccion):
        r = (a*(1-e**2))/(1+e*np.cos(phi))
        #r = (1*(1-e**2))/(1+e*np.cos(phi))
        x.append(r*np.cos(phi))
        y.append(r*np.sin(phi))
        distancia= (x[cuenta]**2 + y[cuenta]**2)**(1/2)
        if distancia>apo:
            apo = distancia
            coordenadas_apo["x"]=x[cuenta]
            coordenadas_apo["y"]=y[cuenta]
        elif distancia<perio:
            perio=distancia
            coordenadas_perio["x"]=x[cuenta]
            coordenadas_perio["y"]=y[cuenta]
    resultado.append(x)
    resultado.append(y)
    resultado.append(apo)
    resultado.append(perio)
    resultado.append(coordenadas_apo)
    resultado.append(coordenadas_perio)
    resultado.append(nombre)
    return resultado

def dibujar_orbita(databas):
    fig = plt.figure()
    ax=fig.add_subplot()
    ax.set_title("Órbita solicitada")
    ax.set_xlabel("Eje X en UA")
    ax.set_ylabel("Eje y en UA")
    ax.set_facecolor('black')
    ax.plot(0,0,marker=f"$✦$",markersize=4,label="Centro de Masa",color="yellow")
    for n in databas:
        database = n
        linea,=ax.plot(database[0],database[1],'-',label = f"Trayectoria de la Orbita {database[6]}")
        ax.legend(loc='lower right',prop={'size': 6})
    point,=ax.plot(0,0,marker=8,color="red",label="Cuerpo en Orbita")
    def update_point(n, x, y,point):
        point.set_data(np.array([x[n], y[n]]))
        return point
    ani=animation.FuncAnimation(fig, update_point, fargs=(database[0], database[1], point),interval=1)
    writergif = animation.PillowWriter(fps=30) 
    ani.save("orbita.gif",writer=writergif)

