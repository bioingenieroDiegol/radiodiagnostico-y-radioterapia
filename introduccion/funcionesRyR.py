import numpy as np
from scipy import constants

def N(n0, tmedio, t):
    '''Calcula la exponencial decreciente que describen los núcleos radiactivos al decaer
    n0: núcleos iniciales
    tmedio: semiperíodo de desintegración del radionucleido
    t: tiempo
    '''
    lmbd = np.log(2)/tmedio
    exponente = - lmbd * t
    return n0 * np.exp(exponente)

def A(a0, tmedio, t):
    '''Calcula la exponencial decreciente que describe la actividad
    a0: actividad inicial
    tmedio: semiperíodo de desintegración del radionucleido
    t: tiempo
    '''
    lmbd = np.log(2)/tmedio
    exponente = - lmbd * t
    return a0 * np.exp(exponente)

def tmedio2lambda(tmedio):
    '''Convierte el semiperíodo de desintegración en la constante de desintegración'''
    return np.log(2)/tmedio

def lmbd(x, x0, t):
    '''Calcula la constante de desintegración siendo:
    x: la actividad o el número de nucleos en un tiempo t
    x0: la actividad inicial o el número de nucleos en t=0'''
    a = -1 / t
    b = np.log(x/x0)
    return a*b 

def A2N(a, lmbd):
    '''Convierte la actividad instantánea en el número de núcleos presentes en la muestra en ese instante
    a: actividad actual
    tmedio: semiperíodo de desintegración del radionucleido
    '''
    return a/lmbd

def N2A(n, lmbd):
    '''Convierte el número de nucleos de una muestra en la actividad correspondiente'''
    return n * lmbd
    
def N2masa(N, masa_atomica):
    '''Convierte el número de nucleos en la masa que les corresponde'''
    return masa_atomica * N / constants.Avogadro

def masa2N(masa, masa_atomica):
    '''Convierte la masa de una muestra en el número de nucleos presentes'''
    return masa * constants.Avogadro / masa_atomica
    
def concAct(a, vol):
    '''Calcula la concentración de actividad en una solución
    a: actividad
    vol: volumen de solución'''
    return a/vol

def mostrar(numero,precision=2):
    '''Esta función permite darle formato científico a un número. El argumento
    *precision* es la cantidad de decimales con que se verá.
    '''    
    print( "{:.{}e}".format(numero, precision ) )
    
# definimos los puntos iniciales y finales como tuplas
# p1 = (1, 5)
# p2 = (3, 10)

# definimos la función de interpolación lineal
def interpolar(pi, pf, x):
    deltaY = pf[1] - pi[1]
    deltaX = pf[0] - pi[0]
    return (x - pi[0]) * deltaY / deltaX + pi[1]

def interpolar2(xi,yi,xf,yf,x):
    deltaY = yf - yi
    deltaX = xf - xi
    return (x - xi) * (deltaY / deltaX) + yi