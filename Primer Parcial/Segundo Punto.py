"""
Escriba un programa que simule un juego de dados entre dos jugadores (Alejandro y
Beatriz). Cada jugador lanza dos dados. Si no coincide ningún dado, gana Alejandro. Si
coincide uno de los dados, gana Beatriz. Si coinciden los dos dados, empatan
"""

import random

dadoAlejandro = [1,1]
dadoBeatriz = [1,1]

for x in range(100):
    dadoAlejandro[0] = random.randint(1,6)
    dadoAlejandro[1] = random.randint(1,6)
    dadoBeatriz[0] = random.randint(1,6)
    dadoBeatriz[1] = random.randint(1,6)

    print("\nJUEGO DE DADOS")
    print("\nAlejandro ha sacado",dadoAlejandro[0], "y",dadoAlejandro[1])
    print("\nBeatriz ha sacado",dadoBeatriz[0], "y",dadoBeatriz[1])

    if ( dadoBeatriz[0] == dadoAlejandro[0] ):
        
        if( dadoBeatriz[1] == dadoAlejandro[1] ):
            print("\nHan empatado.")
        else:
            print("\nHa ganado Beatriz.")

    elif ( dadoBeatriz[0] == dadoAlejandro[1] ):
        
        if( dadoBeatriz[1] == dadoAlejandro[0] ):
            print("\nHan empatado.")
        else:
            print("\nHa ganado Beatriz.")

    elif ( dadoBeatriz[1] == dadoAlejandro[0] ): 

        if( dadoBeatriz[0] == dadoAlejandro[1] ):
            print("\nHan empatado.")
        else:
            print("\nHa ganado Beatriz.")

    elif ( dadoBeatriz[1] == dadoAlejandro[1] ):
        
        if( dadoBeatriz[0] == dadoAlejandro[0] ):
            print("\nHan empatado.")
        else:
            print("\nHa ganado Beatriz.")
    
    else:
        print("\nHan ganado Alejandro.")