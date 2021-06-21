from tkinter import *
from tkinter import ttk, messagebox, font

class Aplicacion():
    __ventana = None
    __altura = None
    __peso = None
    __imc = None
    __composicion = None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('340x220')
        self.__ventana.title('Calculadora de IMC')
        self.__ventana.resizable(0, 0)
        self.__altura = StringVar()
        self.__peso = StringVar()
        self.__imc = StringVar()
        self.__composicion = StringVar()

        ttk.Label(text="Calculadora de IMC").grid(column=0, row=0, columnspan=2)
        framel = ttk.Frame(self.__ventana, borderwidth=2,relief="solid", padding=(10,10))
        framel.grid(column=0, row=1, columnspan=2)
        framel.columnconfigure(0, weight=1)
        framel.rowconfigure(0, weight=1)

        ttk.Label(framel, text="Altura:").grid(column=0, row=0)
        self.altura = ttk.Entry(framel, width=40, textvariable=self.__altura)
        self.altura.grid(column=1, row=0)
        ttk.Label(framel, text="cm").grid(column=2, row=0)

        ttk.Label(framel, text="Peso:").grid(column=0, row=1)
        self.peso = ttk.Entry(framel, width=40, textvariable=self.__peso)
        self.peso.grid(column=1, row=1)
        ttk.Label(framel, text="kg").grid(column=2, row=1)
        for hijo in framel.winfo_children():
            hijo.grid_configure(padx=10, pady=10)
        ttk.Button(self.__ventana, text="Calcular", command=self.calcular).grid(column=0, row=2, pady=10)
        ttk.Button(self.__ventana, text="Limpiar", command=self.limpiar).grid(column=1, row=2, pady=10)
        frameresult = ttk.Frame(self.__ventana, borderwidth=1,relief="solid")
        frameresult.grid(column=0, row=3, columnspan=2)
        frameresult.columnconfigure(0, weight=1)
        frameresult.rowconfigure(0, weight=1)

        fuente = font.Font(size=10, weight='bold', slant="italic")
        ttk.Label(frameresult, text="Tu indice de masa corporal es:").grid(column=0, row=0)
        ttk.Label(frameresult, textvariable=self.__imc, font=fuente).grid(column=1, row=0)
        ttk.Label(frameresult, textvariable=self.__composicion, font=fuente).grid(column=0, row=1, columnspan=3)

        self.altura.focus()
        self.__ventana.mainloop()


    def calcular(self):
        try:
            altura = float(self.altura.get()) / 100
            peso = float(self.peso.get())
            imc = peso / altura ** 2
            imc = round(imc, 2)
            if imc < 18.5:
                composicion = "Peso inferior al normal"
            elif imc >= 18.5 and imc < 25:
                composicion = "Peso normal"
            elif imc >= 25 and imc < 30:
                composicion = "Peso superior al normal"
            else:
                composicion = "Obesidad"
            self.__imc.set(str(imc) + ' kg/m2')
            self.__composicion.set(composicion)
        except ValueError:
            messagebox.showerror(title='Error de tipo', message='Debe ingresar valores numericos')

    def limpiar(self):
     self.__altura.set('')
     self.__peso.set('')
     self.__composicion.set('')
     self.__imc.set('')

if __name__ == '__main__':
 mi_app = Aplicacion()