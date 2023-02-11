print("Escoga un numero, pulse enter, despues elija su ponderacion y pulse enter hasta que haya escogido 3 numeros. La suma de su ponderacion no puede ser mayor que 100")
numero1 = int(input())
ponderacion1 = int(input())
numero2 = int(input())
ponderacion2 = int(input())
numero3 = int(input())
ponderacion3 = int(input())
def f1(funcion_parametro):
    def funcion_interior():
        print("Ahora, calcularemos la media ponderada de estos tres")
        funcion_parametro()
        print("La media ponderada de los 3 numeros que ha escogido es", media_ponderada)
    return funcion_interior
@f1
def media_ponderada():
    media_ponderada = (numero1*ponderacion1+numero2*ponderacion2+numero3*ponderacion3)/(ponderacion1+ponderacion2+ponderacion3)
    return media_ponderada