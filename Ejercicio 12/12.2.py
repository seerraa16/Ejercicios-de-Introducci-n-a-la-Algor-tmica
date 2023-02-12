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
        print("Se ha ingresado", cantidad, "€ en la cuenta de", self.nombre)
        print("El saldo actual es de", self.saldo, "€")
    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("No se puede retirar esa cantidad")
        else:
            self.saldo -= cantidad
            print("Se ha retirado", cantidad, "€ de la cuenta de", self.nombre)
            print("El saldo actual es de", self.saldo, "€")
    def transferir(self, cantidad, cuenta):
        if cantidad > self.saldo:
            print("No se puede transferir esa cantidad")
        else:
            self.saldo -= cantidad
            cuenta.saldo += cantidad
            print("Se ha transferido", cantidad, "€ de la cuenta de", self.nombre, "a la cuenta de", cuenta.nombre)
            print("El saldo actual de", self.nombre, "es de", self.saldo, "€")
            print("El saldo actual de", cuenta.nombre, "es de", cuenta.saldo, "€")
    def consultar_mi_saldo(self):
        print("El saldo actual de", self.nombre, "es de", self.saldo, "€")
    