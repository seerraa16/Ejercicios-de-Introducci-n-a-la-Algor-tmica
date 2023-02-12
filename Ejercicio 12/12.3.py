class cuenta_bancaria:
    def __init__(self, nombre, dni, IBAN, contraseña, saldo):
        self.nombre = nombre
        self.dni = dni
        self.IBAN = IBAN
        self.contraseña = contraseña
        self.saldo = saldo
    
    #OPERACIONES
    def ingresar(self, cantidad):
        self.saldo += cantidad
        print("has metido", cantidad, "€ en su cuenta")
        print("tiene: ", self.saldo, "€")
    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("jajajaja no tienes tanto dinero")
        else:
            self.saldo -= cantidad
            print("has cogido", cantidad, "€")
            print("le quedan", self.saldo, "€")
    def transferir(self, cantidad, cuenta):
        if cantidad > self.saldo:
            print("jajaja no hay tanto dinero")
        else:
            self.saldo -= cantidad
            cuenta.saldo += cantidad
            print("Se ha transferido", cantidad, "€ de la cuenta de", self.nombre, "a la cuenta de", cuenta.nombre)
            print("El saldo actual de", self.nombre, "es de", self.saldo, "€")
            print("El saldo actual de", cuenta.nombre, "es de", cuenta.saldo, "€")
    def consultar_mi_saldo(self):
        print("solo le quedan: ", self.saldo, "€")