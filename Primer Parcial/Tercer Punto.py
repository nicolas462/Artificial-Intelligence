"""
Escriba un programa que pida la longitud de los tres lados de un triángulo (empezando por
el lado más largo) y escriba si el triángulo es imposible (si el lado más largo es mayor que
los otros dos juntos), posible, o degenerado (si el lado más largo mide lo mismo que los
otros dos juntos).
"""

#Retorna True, si el @lado es más largo que @ladoLargo.
def isLarger(lado, ladoLargo):
    if (lado > ladoLargo):
            print("\n¡Le he pedido que escribiera primero el lado más largo!")
            return True
    return False

isInteger = True

#Cuando se ingresa un valor distitno a un Integer, el while termina.
while isInteger:
    print("\nANALIZADOR DE TRIÁNGULOS")
    ladoLargo = input("\nEscriba la longitud del lado más largo: ")

    try:
        #convierte la entrada a un int.
        ladoLargo = int(ladoLargo)

        if (ladoLargo < 0):
            print("\n¡El valor debe ser positivo!")
        
        else:
            segundoLado = int(input("\nEscriba la longitud del segundo lado: "))

            if (isLarger(segundoLado, ladoLargo)):
                continue

            tercerLado = int(input("\nEscriba la longitud del tercer lado: "))

            if (isLarger(tercerLado, ladoLargo)):
                continue
            
            if (segundoLado + tercerLado > ladoLargo):
                print("\nUn triángulo puede tener como lados {}, {} y {}.".format(ladoLargo,segundoLado,tercerLado))
            
            elif (segundoLado + tercerLado == ladoLargo):
                print("\nLos datos corresponden a un triángulo degenerado.")

            else:
                print("\nUn triángulo puede no tener como lados {}, {} y {}.".format(ladoLargo,segundoLado,tercerLado))


    except ValueError:  # si la entrada no es un int.
        print("\nEntrada no válida. Programa finalizado.")
        isInteger = False