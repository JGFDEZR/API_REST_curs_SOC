#!/usr/bin/python3

# Definim una classe base "cotxe"
class Cotxe():
    def __init__(self, marca, model, any):
        self.marca = marca
        self.model = model
        self.any = any
        
    def accelerar(self):
        print("El cotxe està accelerant.")
    
    def frenar(self):
        print("El cotxe està frenant.")

    def __str__(self):
        return f"{self.marca=}, {self.model=}, {self.any=}"
        
# Definim una subclasse "cotxe_esportiu" que hereta de "cotxe"
class Cotxe_amb_canvi_manual(Cotxe):
    def __init__(self, marca, model, any, qty_marxes):
        super().__init__(marca, model, any)
        self.qty_marxes = qty_marxes
        
    def canviar_marxa(self):
        print("El cotxe està canviant de marxa.")

if __name__ == "__main__":
    un_cotxe = Cotxe("Chevrolet", "Camaro", 2020)
    un_cotxe_amb_canvi_manual = Cotxe_amb_canvi_manual("Ford", "Courier", 2017, 5)

    print(f"{str(un_cotxe)=}")
    print(f"{str(un_cotxe_amb_canvi_manual)=}")

