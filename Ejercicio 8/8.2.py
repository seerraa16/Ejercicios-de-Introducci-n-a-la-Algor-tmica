def intereses(capital, interes, tiempo):
    return capital * interes * tiempo
    for i in range(1, tiempo + 1):
        capital = capital + intereses(capital, interes, i)  
    return capital
def funcion_decoradora(funcion_parametro):
    def funcion_interior():
        print("El capital final es: ", capital_final)
    return funcion_interior
@funcion_decoradora
def capital_final():
    pass
capital_final()
