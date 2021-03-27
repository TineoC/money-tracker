import tkinter 
from tkinter import simpledialog, messagebox
import tkinter.font as tkFont
import tkinter.ttk as ttk

ventana1 = tkinter.Tk()
ventana1.geometry("800x600")
style = ttk.Style()
style.theme_use("xpnative")
montolist = []
ventana1.configure(background = "#F7F4F3")

hStyle = ttk.Style()
hStyle.configure("header.TFrame", background = "#F7F4F3")

cStyle = ttk.Style()
cStyle.configure("cuerpo.TFrame", borderwidth=5)


# class Entrada:
#     def __init__ (self, monto):
#         self.monto = monto

#     def añadirEntrada(self,monto):
#         labelMonto = ttk.Label(ventana1,text = monto)
#         labelMonto.pack()

#metodo 1 de hacer un popup (basicamente una nueva ventana en verdad...), puedo crear un label nuevo en la ventana 1 o updatear uno ya existente... 
def cambio():
    popUp = tkinter.Toplevel(ventana1)
    popUp.geometry("200x200")

    label = ttk.Label(popUp, text = "Añadir entrada:")
    textbox = ttk.Entry(popUp)

    def añadirEntrada():
        try:
             monto = int(textbox.get())
        except : 
            messagebox.showerror("ERROR","Debe ingresar un NUMERO")
            return
        montolist.append(monto)
        #en vez de usar lista, usar el write y readall de un txt para imprimirlo entero en el label 
        label2 = ttk.Label(cuerpoFrame, text = montolist) 
        label2.grid(row = 1, column = 0)

    label.grid(row=0, column = 0)
    textbox.grid(row=1, column = 0)

    boton2 = ttk.Button(popUp, text = "Guardar", command = añadirEntrada)
    boton2.grid(row=2, column = 0)

# metodo 2, que seria un popup solo para un input basico...   
# def cambio():
#     monto = simpledialog.askinteger(title="Test", prompt="What's your Name?:")
#     label2["text"] = monto

#HEADER
headerFrame = ttk.Frame(ventana1,width = 600, height = 50, style="header.TFrame")
headerFrame.grid(row = 0, column = 0, padx = 5, pady = 10) 

inicio = ttk.Label(headerFrame, text = "INICIO", foreground = "#1E5871", background = "#F7F4F3", font = "30")
inicio.grid(row = 0, column = 0)

separador = ttk.Separator(ventana1, orient = "horizontal")
separador.place(x=0, y=40, relwidth=1)

#CUERPO
cuerpoFrame = ttk.Frame(ventana1, width = 600, height = 50, relief = "solid", borderwidth = 2)
cuerpoFrame.grid(row = 2, column = 0, padx = 10, pady = 10) 

boton = ttk.Button(cuerpoFrame, text = "Añadir entrada",command = cambio)
boton.grid(row=0, column = 0,padx = 10, pady = 10)

ventana1.mainloop()