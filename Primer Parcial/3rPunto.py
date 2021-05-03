import math
respuesta = ""
while respuesta != "no":
    print ("Introduzca las componentes HSL:")
    try:
        Matiz = int(input("Matiz (entero de 0 a 360) H ="))
        pruebaM = int(Matiz)
        if Matiz < 0 or Matiz > 360:
            print("Matiz incorrecto. Inténtelo de nuevo.")
            continue
    except ValueError:
        print("Matiz incorrecto. Inténtelo de nuevo.")
        continue
    try:
        Saturacion = float (input("Saturación (decimal de 0 a 1) S ="))
        pruebaS = float(Saturacion)
        if Saturacion < 0 or Saturacion > 1:
            print("Saturacion incorrecta. Inténtelo de nuevo.")
            continue
    except ValueError:
        print("Saturacion incorrecta. Inténtelo de nuevo.")
        continue
    try:
        Luminosidad = float(input("Luminosidad (decimal de 0 a 1) L = "))
        pruebaL = float(Luminosidad)
        if Luminosidad < 0 or Luminosidad > 1:
            print("Luminosidad incorrecta. Inténtelo de nuevo.")
            continue
    except ValueError:
        print("Luminosidad incorrecta. Inténtelo de nuevo.")
        continue
        R = ""
        G = ""
        L = ""
    if Matiz == 0 and Saturacion == 0 :
        R = int(Luminosidad * 255)
        G = R
        B = G
        print ("El color es R = " + str(R) + ", G = " + str(G) + ", B = " + str(B))
        continue
    if Luminosidad < 0.5:
        temp1 = Luminosidad * (1.0 + Saturacion)
    elif Luminosidad >= 0.5:
        temp1 = Luminosidad + Saturacion - Luminosidad * Saturacion
    temp2 = 2 * Luminosidad - temp1
    Hue = Matiz / 360
    TempR = Hue + 0.333
    TempG = Hue
    TempB = Hue-0.333
    if TempR < 0:
        TempR += 1
    elif TempR > 1:
        TempR -= 1
    if TempG < 0:
        TempG += 1
    elif TempG > 1:
        TempR -= 1
    if TempB < 0:
        TempB += 1
    elif TempB > 1:
        TempB -= 1
    if 6 * TempR <1:
        R = temp2 + (temp1 - temp2 ) * 6 * TempR
        R  = math.floor(R * 255)
    elif 2 * TempR < 1 :
        R = temp1
        R  = math.floor(R * 255)
    elif 3 * TempR < 2:
        R = temp2 + (temp1 -  temp2) * (0.666 - TempR) * 6
        R  = math.ceil(R * 255)
    else:
        R = temp2
        R  = math.ceil(R * 255)
    if 6 * TempG <1:
        G = temp2 + (temp1 - temp2 ) * 6 * TempG
        G  = math.ceil(G * 255)
    elif 2 * TempG < 1 :
        G = temp1
        G  = math.floor(G * 255)
    elif 3 * TempG < 2:
        G = temp2 + (temp1 -  temp2) * (0.666 - TempG) * 6
        G  = math.ceil(G * 255)
    else:
        G = temp2
        G  = math.ceil(G * 255)
    if 6 * TempB <1:
        B = temp2 + (temp1 - temp2 ) * 6 * TempB
        B  = math.ceil(B * 255)
    elif 2 * TempB < 1 :
        B = temp1
        B  = math.ceil(B * 255)
    elif 3 * TempB < 2:
        B = temp2 + (temp1 - temp2) * (0.666 - TempB) * 6
        B = math.floor(B * 255)
    else:
        B = temp2
        B  = math.ceil(B * 255)
    print ("El color es R = " + str(R) + ", G = " + str(G) + ", B = " + str(B))




