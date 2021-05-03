"""
Quizás Jack Aubrey, durante su encierro en Algeciras, pudo pasar las horas muertas
jugando solitarios con los dados. Uno de estos solitarios consiste en tirar una cantidad de
dados y sumar los puntos de los dados en los que se obtiene el mismo valor. La puntuación
obtenida es el valor más alto.
"""
import random

# Obtiene la puntuación mayor de los datos dado un
# diccionario de datos (@values).
def getBiggestScore(values):
    biggest = 0

    for x in values:
        value = values.get(x)
        if (value > biggest):
            biggest = value
    
    return biggest

isInteger = True

#Cuando se ingresa un valor distitno a un Integer, el while termina.
while isInteger:
    print("\nJUEGO DADOS REPETIDOS")
    dados = input("\n¿Cuántos dados quiere tirar? ")

    try:
        #convierte la entrada a un int.
        dados = int(dados)

        if (dados <= 0):
            print("¡Debe tirar al menos un dado!")
            continue
        
        else:
            dadosLanzados = {}

            for x in range(dados):
                dadoRandom = random.randint(1,6)
                getValor = dadosLanzados.get(dadoRandom)

                print("Dado {}: {}".format(x+1, dadoRandom))

                # Si el número generado no se encuentra en el diccionario.
                if ( getValor is None ):
                    dadosLanzados[dadoRandom] = dadoRandom
                else:
                    dadosLanzados.update({dadoRandom: (getValor+dadoRandom)})
            
            print("Has obtenido {} puntos.".format(getBiggestScore(dadosLanzados)))


    except ValueError:  # si la entrada no es un int.
        print("\nEntrada no válida. Programa finalizado.")
        isInteger = False