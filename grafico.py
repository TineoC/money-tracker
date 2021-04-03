def calcularTotales():

    totalCategorias = {
        "Comida": 0,
        "Entretenimiento": 0,
        "Servicios": 0,
        "Ropa": 0,
        "Sueldo": 0,
        "Prestamo": 0,
        "Venta": 0
    }

    with open("historial.txt", "r") as historial:
        lines = historial.readlines()

    i = 0

    for line in lines:
        line = line.rstrip('\n')
        if line in totalCategorias.keys():
            totalCategorias[line] = int(lines[i+1].rstrip('\n'))
        i += 1

    return totalCategorias


def generar():
    total = calcularTotales()
