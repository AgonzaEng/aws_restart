#Escribe un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

horas = float(input("Ingrese número de horas trabajadas"))
costo = float(input("Ingrese el pago por hora"))
pago = horas * costo
print("El valor a pagaa al empleado es: ", pago)

