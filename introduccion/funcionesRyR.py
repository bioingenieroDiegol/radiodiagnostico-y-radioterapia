import numpy as np

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

def AtoN(a, tmedio):
    '''Convierte la actividad instantánea en el número de núcleos presentes en la muestra en ese instante
    a: actividad actual
    tmedio: semiperíodo de desintegración del radionucleido
    '''
    lmbd = np.log(2)/tmedio
    return a/lmbd
    
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