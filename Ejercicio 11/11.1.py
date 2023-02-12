print("Calcularemos cuanto es el sueldo que debe cobrar un empleado segun sus horas extras")
print("Ingrese la cantidad de horas que trabajo el empleado")
horas = int(input())
print("ingrese su suedo bruto")
sueldo = int(input())
if horas >= 44:
    print("El empleado debe cobrar", (sueldo)/35*1.5*(horas-35), "€ por las horas extras")
elif horas >= 36 and horas<= 43:
    print("El empleado debe cobrar", (sueldo)/35*1.25*(horas-35), "€ por las horas extras")
elif horas <=35:
    print("El empleado no debe cobrar nada por las horas extras")

