from tkinter import *
from tkinter import ttk, messagebox

class Aplicacion:
    __ventana=None
    
    def __init__(self):
        self.__ventana=Tk()
        self.__ventana.title("Calculo de IVA")
        self.__ventana.resizable(0,0) 
        self.marco=ttk.Frame(self.__ventana,padding=(10,10))
        
        
        self.sinivaLbl=ttk.Label(self.__ventana,text="Precio sin IVA").grid(row=0,column=0)
        self.siniva=StringVar()
        self.conivaLbl=ttk.Label(self.__ventana,text="Precio con IVA").grid(row=4,column=0)
        self.coniva=StringVar()
        self.ivaLbl=ttk.Label(self.__ventana,text="IVA").grid(row=3,column=0)
        self.iva=StringVar()
        self.ctext1=ttk.Entry(self.__ventana,textvariable=self.siniva,width=10).grid(row=0,column=1)
        self.ctext2=ttk.Entry(self.__ventana,textvariable=self.iva,width=10).grid(row=3,column=1)
        self.ctext3=ttk.Entry(self.__ventana,textvariable=self.coniva,width=10).grid(row=4,column=1)
        self.valor= IntVar()
        self.boton1=ttk.Button(self.__ventana,text="Calcular",command=self.calcular).grid(row=5,column=0)
        self.boton2=ttk.Button(self.__ventana,text="Salir",command=quit).grid(row=5,column=1)
        
        self.iva21=ttk.Radiobutton(self.__ventana, text="IVA 21%",value=0,variable=self.valor).grid(column=0,row=1)
        self.iva10=ttk.Radiobutton(self.__ventana, text="IVA 10.5%",value=1,variable=self.valor).grid(column=0,row=2)
        
        
        
        self.__ventana.mainloop()
    
          
    def calcular (self):
            v=float (self.siniva.get())
            if self.valor.get()==0:
                 i=(v *21)/100
                 self.iva.set(i)
                 self.coniva.set(i+v)
            else:
                 if self.valor.get()==1:
                      i=(v*10.5)/100
                      self.iva.set(i)
                      self.coniva.set(i+v)
            self.siniva.set('')


