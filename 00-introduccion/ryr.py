# lista con partículas: electrones Auger y electrones de conversión.
particulas = ["Au", "ce"]
# lista con fotones: gammas y rayos X.
fotones = ["γ ", "Kα", "Kβ", ]


def convertirEnergia(energia):
    '''Elimina el último caracter de la cadena energía
    si es que se trata de un asterisco'''
    if energia[-1]=='*':
        energia = energia[:-1]
    return float(energia)


def clasifica(emision):
    '''Clasifica la emisión (ingresada como string) usando las primeras dos
    letras de su nombre. Puede ser una partícula, un fotón o si se desconoce
    se devuelve el valor "desconocida".
    '''    item = emision[0:2]
    soy = 'desconocida'
    if item in particulas:
        soy = "partícula"
    elif item in fotones:
        soy = "fotón"
    return soy


def plustwo(n):
    out = n + 2
    return out