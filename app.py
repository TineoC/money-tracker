import tkinter
from tkinter import simpledialog, messagebox, NORMAL, DISABLED, END
import tkinter.font as tkFont
import tkinter.ttk as ttk
from ttkthemes import ThemedStyle

import grafico

ventanaPrincipal = tkinter.Tk()
ventanaPrincipal.geometry("800x600")
# Deshabilita el resizing de la pantalla (no permite hacer la ventana más grande o más pequeña) para que no se descoloquen los widgets
ventanaPrincipal.resizable(width=False, height=False)
ventanaPrincipal.title("Money Tracker")

style = ThemedStyle()
style.set_theme("arc")

ventanaPrincipal.configure(background="#F7F4F3")
latoBig = tkFont.Font(family="Lato", size=12)

hStyle = ttk.Style()
hStyle.configure("header.TFrame", background="#F7F4F3")

# Variables (tkinter tiene un bug, no toma las textvariable para entry si no son globales)
tituloDefault = tkinter.StringVar()
# tituloDefault.set("Titulo...")
montoDefault = tkinter.StringVar()
# montoDefault.set("Monto...")

# Calculamos el balance por si no es la primera vez que se inicia la app.
global balance
balance = 0
with open("historial.txt", "r") as historial:
    for line in historial:
        line = line.rstrip('\n')
        if line.isnumeric():
            balance += int(line)
        elif line.lstrip("-").isnumeric():
            balance -= -int(line)
        else:
            continue

# Funcion que crea la ventana PopUp, sus widgets etc.


def ventanaEntrada():
    tituloDefault.set("Titulo...")
    montoDefault.set("Monto...")
    # funcion que sera ejecutada por el boton para guardar la entrada del usuario

    def añadirEntrada():
        try:
            monto = int(textbox.get())
        except:
            # En caso del usuario no escribir un número en el input de monto imprimir error
            messagebox.showerror("ERROR", "Debe ingresar un NUMERO")
            popUp.destroy()  # Quitar el popup
            return

        # Escrbir las entradas en el archivo historial en caso de ser correctas
        with open("historial.txt", "a") as historial:
            historial.write(titulo.get()+"\n")
            historial.write(opcion.get()+"\n")
            historial.write(str(monto)+"\n")
            historial.write(
                "------------------------------------------------------------------------------------------------------------------------"+"\n")
        Text.config(state=NORMAL)
        Text.delete("1.0", END)
        with open("historial.txt", "r") as historial:
            for line in historial:
                Text.insert(END, line)
        Text.config(state=DISABLED)
        popUp.destroy()

    # Creación de la ventana que saldra como pop-up
    popUp = tkinter.Toplevel(ventanaPrincipal)  # Desplegar ventana de entrada
    popUp.geometry("300x150")
    popUp.resizable(width=False, height=False)  # No permitir resizing
    popUp.title("Añadir Entrada...")

    # lista con filtros default (para que el usuario cree los suyos
    # podemos hacer que se lea esta lista desde un txt y dar la opcion de
    # que el usuario escriba una etiqueta y se añada al txt como guardado)
    filtros = ["Comida", "Entretenimiento", "Servicios",
               "Ropa", "Sueldo", "Prestamo", "Venta"]

    # label que indica al usuario lo que debe hacer + caja de texto (entry) donde ingresará el valor del monto
    textbox = ttk.Entry(popUp, textvariable=montoDefault, justify="center")
    titulo = ttk.Entry(popUp, textvariable=tituloDefault, justify="center")

    # variable que almacenara nuestra opcion para el filtro en el selector
    opcion = tkinter.StringVar()
    # opcion.set(filtros[0])

    # creamos el optionbox (selector)
    selectorFiltro = ttk.OptionMenu(popUp, opcion, filtros[0], *filtros)

    guardarEntrada = ttk.Button(popUp, text="Guardar", command=añadirEntrada)

    # Colocamos los elementos de nuestra ventana en el grid de la misma para que se muestren al usuario
    titulo.grid(row=0, column=0, padx=15)
    textbox.grid(row=0, column=1, pady=20)  # ese pad afecta al row entero
    selectorFiltro.grid(row=1, column=0)
    guardarEntrada.grid(row=1, column=1, pady=10)

# metodo 2, que seria un popup solo para un input basico...
# def ConfigBalance():
#     balance = simpledialog.askinteger(title="Configurar balance...", prompt="Balance:")
#     conBalance = balance


# HEADER
headerFrame = ttk.Frame(ventanaPrincipal, width=600,
                        height=50, style="header.TFrame")
headerFrame.grid(row=0, column=0, padx=5, pady=10)

inicio = ttk.Label(headerFrame, text="INICIO",
                   foreground="#1E5871", background="#F7F4F3", font=latoBig)
inicio.grid(row=0, column=0)

separador = ttk.Separator(ventanaPrincipal, orient="horizontal")
separador.place(x=0, y=40, relwidth=1)

# CUERPO
cuerpoFrame = ttk.Frame(ventanaPrincipal, width=600,
                        height=50, relief="solid", borderwidth=1)
cuerpoFrame.grid(row=1, column=0, padx=30, pady=10)

boton = ttk.Button(cuerpoFrame, text="Añadir entrada", command=ventanaEntrada)
boton.grid(row=0, column=0, padx=10, pady=10)

Text = tkinter.Text(cuerpoFrame, font=latoBig, state=DISABLED, height="20")
Text.grid(row=1, column=0)

# Anotamos el contenido de historial.txt en la textbox por si no es la primera vez que se inicia la app
Text.config(state=NORMAL)
with open("historial.txt", "r") as historial:
    for line in historial:
        Text.insert(END, line)
Text.config(state=DISABLED)

# FUNCIONES ventanaPrincipal

# Calcula el balance y actualiza la etiqueta para mostrar al usuario la cantidad


def CalcularBalance():
    balance = 0
    with open("historial.txt", "r") as historial:
        for line in historial:
            line = line.rstrip('\n')
            if line.isnumeric():
                balance += int(line)
            elif line.lstrip("-").isnumeric():
                balance -= -int(line)
            else:
                continue
    balanceLabel["text"] = "Balance: " + str(balance)

# Borra el contenido del archivo "historial.txt" y limpia la caja de texto que muestra las entradas.


def BorrarHistorial():
    with open("historial.txt", "w") as historial:
        historial.truncate()
    Text.config(state=NORMAL)
    Text.delete("1.0", END)
    Text.config(state=DISABLED)


# BOTTOM
bottomFrame = ttk.Frame(ventanaPrincipal, width=800,
                        height=50, style="header.TFrame")
bottomFrame.grid(row=2, column=0, sticky="W")
# Label que muestra el balance actual
balanceLabel = ttk.Label(bottomFrame, text="Balance: " + str(balance),
                         font=latoBig, foreground="#1E5871", background="#F7F4F3")
balanceLabel.grid(row=0, column=0, padx="30", sticky="W")
# Boton que actualiza/calcula el balance en base a las entradas del usuario
botonBalance = ttk.Button(
    bottomFrame, text="Calcular Balance", command=CalcularBalance)
botonBalance.grid(row=1, column=0, padx="30", pady="10", sticky="W")
# Boton que borra el contenido de historial.txt
botonBorrar = ttk.Button(
    bottomFrame, text="Borrar Historial", command=BorrarHistorial)
botonBorrar.grid(row=1, column=1, sticky="W")

botonGenerarGrafico = ttk.Button(
    bottomFrame, text="Generar Gráfico", command=grafico.generar)
botonGenerarGrafico.grid(row=1, column=2, padx="30", sticky="W")

ventanaPrincipal.mainloop()