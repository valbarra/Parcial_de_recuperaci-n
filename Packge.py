from Person import *
class paquete:
    def __init__(self, contenido:str, trasnporte:str, cost:float, estado:str, direccion_entrega:str, paquetes, ID:int, peso:float) -> None:
        self.contenido = contenido
        self.transporte = trasnporte
        self.cost = cost
        self.estado = estado
        self.direccion_entrega = direccion_entrega
        self.id = ID
        self.peso = peso
        self.paquetes = list [paquete] = []
    
    def append_paquetes (self):
        self.paquetes.append (paquete)

    def show_paquetes (self):
        paquete = None
        for paquete in self.paquetes:
            print (f'{self.id} - {self.peso} - {self.direccion_entrega} - {self.cost}')