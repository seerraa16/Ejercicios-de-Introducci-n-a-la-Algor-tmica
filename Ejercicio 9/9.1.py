print("Escoga un numero y pulse enter hasta que haya escogido 3 numeros")
numero1 = int(input())
numero2 = int(input())
numero3 = int(input())
def f1(funcion_parametro):
    def funcion_interior():
        print("Vamos a calcular la media de los numeros que ha escogido")
        funcion_parametro()
        print("La media de los numeros que ha escogido es", media)
    return funcion_interior
@f1
def media():
    media = (numero1+numero2+numero3)/3
    return media