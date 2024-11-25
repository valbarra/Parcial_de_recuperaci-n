from Packge import paquete
from Person import Persona, cliente

class app: 
    def star (self) -> None: 
        print ("Bienvenido a Saman Delivery") 

    def create_person(self):
            nombre = input('Por favor ingrese el nombre del cliente: ')
            apellido = input('Por favor ingrese el apellido del cliente: ')
            cedula = input('Por favor ingrese la cedula del cliente: ') 
            telefono = input ('Por favor ingrese numero telefonico del cliente: ')
            direccion = input ('Por favor ingrese la direccion domiciliaria del cliente: ') 
            client = cliente (nombre, apellido, cedula, direccion, telefono)
            self.clientes_append  (client)
            return client 
    def enviar_paquete (sefl):
         contenido = input('Por favor ingrese el contenido del paquete: ')
         transporte = input('Por favor ingrese el tipo de transporte (moto, carro o van): ')
         estado = input('Por favor ingrese el estado destino: ')
         direccion_entrega = input('Por favor ingrese la direccion destino del envio: ')
         ID = input ('Por favor ingrese el id de identificacion del paquete: ')
         peso = input ('Por favor ingrese el peso del paquete en Kg: ') 
    
    def calcular_precio (self):
        peso = None
        transporte = None
        if peso <= 7 and transporte == 'moto':
            cost = peso*2 
        elif peso>= 7 and transporte == 'carro':
            cost = peso*3
        elif peso <= 7 and transporte == 'carro':
            cost = peso*2
        elif peso >= 7 and transporte == 'van':
            cost = peso*4.5
        ganancia = cost + (cost*0.35)
        

    
    
    
    def menu(self):
        ans = 'y'
        while ans == 'y':
            option = input('''
                1. Registrar cliente
                2. Enviar paquete 
                3. Mostrar paquetes  
                4. Mostrar clientes
            ''')  
            
            if option == '1':
                self.create_person()
            elif option == '2':
                self.enviar_paquete()
                self.calcular_precio ()
            elif option == '3':
               
            elif option == '4':
                pass
            print('Error...')
            ans = input('Desea continuar (y/n)?: ').lower()

