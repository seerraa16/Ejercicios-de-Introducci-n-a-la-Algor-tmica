print("Escoga un numero, pulse enter, despues elija su ponderacion y pulse enter hasta que haya escogido 3 numeros y 3 ponderaciones. La suma de su ponderacion no puede ser mayor que 100")
numero1 = int(input())
ponderacion1 = int(input())
numero2 = int(input())
ponderacion2 = int(input())
numero3 = int(input())
ponderacion3 = int(input())
def funcion_decoradora(funcion_parametro):
    def funcion_interior():
        print("Vamos a calcular la media ponderada de los numeros que has escogido")
        funcion_parametro()
        print("La media ponderada es: ", media_ponderada)
    return funcion_interior
@funcion_decoradora
def media_ponderada():
    media_ponderada = ((numero1*ponderacion1)+(numero2*ponderacion2)+(numero3*ponderacion3))/(ponderacion1+ponderacion2+ponderacion3)
