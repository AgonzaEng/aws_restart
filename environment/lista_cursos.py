lista_asignaturas = []
lista_notas = []

x =  int(input("Ingrese el número de asiganturas a registrar: "))
for x in range(x):  
    
    lista_asignaturas.append(input("Ingrese la asignatura que cursó: "))
    lista_notas.append(input("Ingrese la nota que sacó en la asignatura: "))
    
for item in zip (lista_asignaturas, lista_notas):
     print("Yo estudié", item[0],"y he sacado", item[1])
    