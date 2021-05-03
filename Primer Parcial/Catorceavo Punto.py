import webbrowser

# Valores iniciales para el primer rectángulo.
initialX = 10
initialY = 10
initialWidht = 21
initialHeight = 130

ruta = "catorceavo-punto.html"

with open(ruta, mode="w", encoding="utf-8") as fichero:
    print("<!DOCTYPE html>", file=fichero)
    print('<html lang="es">', file=fichero)
    print("<head>", file=fichero)
    print(' <meta charset="utf-8">', file=fichero)
    print(" <title>Catorceavo Punto</title>", file=fichero)
    print(' <meta name="viewport" content="width=device-width, initial-scale=1.0">', file=fichero)
    print("</head>", file=fichero)
    print("", file=fichero)
    print("<body>", file=fichero)
    print(' <svg width="350" height="350" viewBox="0 0 150 150" style="border: black 1px solid">', file=fichero)

    for x in range(8):
        
        positionX = 10 + 14*x
        positionY = 10 + 15*x
        width = 21
        height = 130 - 15*x

        print('     <rect x="',positionX,'" y="',positionY,'" width="',width,'" height="',height,'"'
            +'fill="none" stroke="black" stroke-width="0.3"/>', file=fichero)

    print(" </svg>", file=fichero)
    print(" </br>", file=fichero)
    print(' <svg width="350" height="350" viewBox="0 0 150 150" style="border: black 1px solid">', file=fichero)
    print('     <rect x="0" y="75" width="150" height="75"fill="Blue"/>', file=fichero) #rectángulo
    
    positionX = 0

    for x in range(10):
        
        positionY = 75
        r = 5

        print('     <circle cx="',positionX,'" cy="',positionY,'" r="',r,'" fill="blue"/>', file=fichero)
        positionX = positionX + 10
        print('     <circle cx="',positionX,'" cy="',positionY,'" r="',r,'" fill="white"/>', file=fichero)
        positionX = positionX + 10

    print(" </svg>", file=fichero)    
    print("</body>", file=fichero)
    print("</html>", file=fichero)

webbrowser.open(ruta)