#Escribir un programa que pregunte al usuario una frase y una letra, recorrer la frase en busca de la letra e 
#identificar el numero de veces que aparece la letra en la frase y mostrarlo por pantalla

("Ingrese una frase")
("Ingrese una letra")

frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra ")
contador = 0
for i in frase:
    if i == letra:
        contador += 1
print("La letra {} aparece {} veces en la frase {}.".format(letra, contador, frase))