class Persona:
    def __init__(self, nombre:str, apellido:str, cedula:str, direccion:str, telefono:str) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.cedula =  cedula
        self.direccion = direccion
        self.telefono =  telefono
        

    def show_client (self):
        print  (f'NOMBRE CLIENTE: {self.nombre}')
        print  (f'APELLIDO CLIENTE: {self.apellido}')
        print  (f'CEDULA CLIENTE: {self.cedula}')
        print  (f'TELEFONO CLIENTE: {self.telefono}')
        print  (f'DIRECCION CLIENTE: {self.direccion}')

class cliente (Persona):
    def __init__(self, nombre: str, apellido: str, cedula: str, direccion: str, telefono: str, paquetes:int, clientes) -> None:
        super().__init__(nombre, apellido, cedula, direccion, telefono)
        self.paquetes = paquetes
        self.clientes = list [cliente] = [] 

    def clientes_append (self):
        self.clientes.append (cliente)
