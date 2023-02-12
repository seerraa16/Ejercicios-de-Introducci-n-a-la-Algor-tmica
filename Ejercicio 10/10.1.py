print("Vamos a calcular el area de un triangulo, para ello neceitaremos la base y la altura, introduzca primero la base y despues la altura")
base = float(input("Introduzca la base: "))
altura = float(input("Introduzca la altura: "))
area = (base * altura) / 2
def funcion_decoradora(funcion_parametro):
    def funcion_interior():
        print("El area del triangulo es: ", area)
    return funcion_interior
@funcion_decoradora
def area_triangulo():
    pass
area_triangulo()

