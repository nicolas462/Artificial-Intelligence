import math
 
respuesta = ""
 
while respuesta != "salir":
    print ("\nCONVERTIDOR HSL a RGB\n")
    print ("Introduzca las componentes HSL: ")
    try:
        h = int(input("Matiz (entero de 0 a 360) H = "))
    
    except ValueError:
        print("Entrada no válida. Inténtelo de nuevo.")
        continue
    try:
        s= float (input("Saturación (decimal de 0 a 1) S = "))
    
    except ValueError:
        print("Entrada no válida. Inténtelo de nuevo.")
        continue
    try:
        l= float(input("l(decimal de 0 a 1) L = "))
 
    except ValueError:
        print("Entrada no válida. Inténtelo de nuevo.")
        continue
 
    if h < 0 or h > 360:
        print("Matiz incorrecto. Inténtelo de nuevo.")
        continue
 
    if s< 0 or s> 1:
        print("Saturación incorrecta. Inténtelo de nuevo.")
        continue
 
    if l< 0 or l> 1:
        print("Luminosidad incorrecta. Inténtelo de nuevo.")
        continue
    
    #cálculo de croma
    u = abs(2 * l - 1)
    v = 1 - u
    c = v * s
    h2 = h / 60
 
    #cálculo de x
    y = (h2 % 2) - 1
    z = 1 - abs(y)
    x = c * z
 
    h3 = math.ceil(h2)
 
    #cálculo de rl, gl, bl
    if (h3 == 1):
        r1 = c
        g1 = x
        b1 = 0
    
    elif (h3 == 2):
        r1 = x
        g1 = c
        b1 = 0
 
    elif (h3 == 3):
        r1 = 0
        g1 = c
        b1 = x
 
    elif (h3 == 4):
        r1 = 0
        g1 = x
        b1 = c
 
    elif (h3 == 5):
        r1 = x
        g1 = 0
        b1 = c
    
    elif (h3 == 6):
        r1 = c
        g1 = 0
        b1 = x
 
    else:
        r1 = 0
        g1 = 0
        b1 = 0
 
    m = l - (c/2)
    r = r1 + m
    g = g1 + m
    b = b1 + m
 
    r = round(255*r)
    g = round(255*g)
    b = round(255*b)
 
    print("El color es R = {}, G = {}, B = {}".format(r,g,b))

