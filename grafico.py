import matplotlib.pyplot as plt
from tkinter import messagebox as popUp

def calcularTotales():

    totalGastos = {
        "Comida": 0,
        "Entretenimiento": 0,
        "Servicios": 0,
        "Ropa": 0,
        "Prestamo": 0,
        "Vacaciones": 0,
        "Renta": 0,
        "Gastos Personales": 0,
    }

    for i in range(3, len(lines), 4):
        # Si está en la linea divisora
        # De los montos el index de la categoría y el monto son:
        # Categoría: lines[i - 2]
        # Monto: lines[i - 1]

        categoria = lines[i - 2].rstrip("\n")

        """
        El valor del monto acumúlalo con el valor absoluto ya que si no, estará el menos (-) que pusimos en la lista de entrada:
            Ejemplo:
                Desayuno    fecha
                -200
                A tí solo te interesa el 200, no el (-200). Ya que el gráfico no funciona con valores negativos
        """

        monto = abs(float(lines[i - 1].rstrip("\n")))

        # Primero, prueba si la categoría existe en el diccionario de totalGastos
        try:
            # Añade al diccionario totalCategorías:
            #   Asigna a la key de la categoría de la entrada, el valor del monto en la entrada leída además, acumula ese valor

            totalGastos[categoria] += abs(float(monto))
        except:
            # Si no está, puede ser varia razones:
            # 1. La entrada que recibe, es de Categoría Sueldo
            # 2. La Categoría de Gasto leída, no existe en las keys del diccionario

            # En cualquiera de los casos, se ignorará la línea y seguirá el bucle
            pass

    return totalGastos


def eliminarCeros(dict):
    dictOut = {}
    for x, y in dict.items():
        if y != 0:
            dictOut[x] = y

    return dictOut


def generar():

    with open("historial.txt", "r") as historial:
        global lines
        lines = historial.readlines()

    if len(lines) == 0:
        # Si el historial está vacío:

        popUp.showerror(
            "Error", "Debes colocar al menos una entrada para generar un gráfico"
        )
        return # No imprimas gráfico

    dict = eliminarCeros(calcularTotales())

    labels = dict.keys()
    values = dict.values()

    window = plt.figure()

    window.canvas.set_window_title("Gráfico")

    plt.title("Gastos por Categoría")

    plt.pie(values, labels=labels, autopct="%1.1f%%")

    plt.show()