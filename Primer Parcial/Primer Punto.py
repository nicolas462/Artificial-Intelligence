"""
Para indicar el tiempo transcurrido desde una fecha pasada, los mayas utilizaban la
llamada cuenta larga o serie inicial, en la que se cuenta
en kins, uinals, tuns, katúns y baktúns. Un kin es un día, un uinal son 20 kins, un tun son
18 uinals, un katún son 20 tuns y un baktún son 20 katúns.
Escriba un programa que solicite una cantidad de días y que responda la cuenta larga maya
correspondiente.
"""

kin = 1
uinal = 20*kin
tun = 18*uinal
katun = 20*tun
baktun = 20*katun

cuentaLarga = [baktun, katun, tun, uinal, kin]
resultado = [] #se almacenan la cantidad de kin, unial (...) mientras se hace el calculo.

entrada = 1
isInteger = True

#Cuando se ingresa un valor distitno a un Integer, el while termina.
while isInteger:
    print("\nCUENTA LARGA MAYA")
    entrada = input("\nEscriba una cantidad de días: ")

    try:
        #convierte la entrada a un int
        entrada = int(entrada)
        aux = entrada

        if (entrada < 0):
            print("\nPor favor, no escriba números negativos.")
            continue

        for x in cuentaLarga:
            # Se aproxima hacia abajo el resultado.
            division = int(entrada/x)
            resultado.append(division)
            entrada = entrada - division*x
        
        print()
        print(aux, "días son", resultado[0], "baktún,", resultado[1], "katún,",
                resultado[2], "tun,", resultado[3], "uinal y", resultado[4], "kin.",)
        
        resultado.clear()

    except ValueError:  # si la entrada no es un int
        print("\nEntrada no válida. Programa finalizado.")
        isInteger = False