#Cree una clase CuentaBancaria que contenga los siguientes atributos: numero_cuenta, propietarios y balance.
# Los tres atributos se deben inicializar en el constructor con valores recibidos como parámetros.
#Para la clase CuentaBancaria, cree un método depositar que maneje las acciones de depósito en la cuenta.
#Para la clase CuentaBancaria, cree un método retirar que maneje las acciones de retiro de la cuenta.
#Para la clase CuentaBancaria, cree un método aplicar_cuota_manejo que aplique un porcentaje del 2% sobre el balance de la cuenta
#Para la clase CuentaBancaria, cree un método mostrar_detalles que imprima por consola los detalles de la cuenta bancaria.

class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance) -> None:
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance
        
    def depositar (self, deposito, deposito_cuenta):
        self.deposito = deposito
        self.depsito_cuenta = deposito_cuenta
        deposito_cuenta = self.balance + self.deposito
        
    def retirar (self, retiro, retiro_cuenta):
        self.retiro = retiro
        self.retiro_cuenta = retiro_cuenta
        retiro_cuenta = self.balance - self.retiro
    
    def aplicar_cuota_manejo (self,cuota_manejo, aplicar):
        self.cuota_manejo = cuota_manejo
        self.aplicar = aplicar
        cuota_manejo = 2 / 100
        aplicar = self.balance * (cuota_manejo) 
        
    def mostrar_detalles (self):
        print(CuentaBancaria(self.numero_cuenta, self.propietarios, self.balance))
                  