print("Escriba cual es el precio que quiere poner a su producto")
precio = input(int())
print("el precio de su producto sin impuestos es de", precio , "euros")
@f1
def precio_con_impuestos():
    precio_con_impuestos = precio * 1.21
    
def f1(funcion_parametro):
    def funcion_interior():
        print("Vamos a calcular el precio de su producto con impuestos, aproximando que se añade un impuesto del 21%")
        funcion_parametro()
        print("El precio de su producto con impuestos es de", precio_con_impuestos , "euros")
    return funcion_interior