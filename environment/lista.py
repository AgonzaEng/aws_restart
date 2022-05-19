#Escribir un programa que pida al usuario las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, 
#Historia y Lengua) en una lista y solicitar la nota de cada asignatura en otra lista y luego muestre por pantalla 
#el mensaje Yo estudio la <asignatura> y he sacado <nota>

#subjectsList = ["Matemáticas", "Física", "Química", "historia", "Literatura", "Inglés", "Arte"]
#print(subjectsList)

#asignatura = []
#nota = []
#asignatura = input("Ingrese la asignatura que cursó") 
#nota =  input("Ingrese la nota que sacó en la asignatura")

#print("Yo estudio {} y he sacado {}" .format(asignatura, nota))


subjects_list = []
score_list = []
num_subjects = int(input("Ingrese el numero de materias: "))

count=0
while count < num_subjects :
    subjects_list.append(input("Ingrese el nombre de la materia: "))
    score_list.append(input("Ingrese su calificacion: "))
    count +=1

i = 0
j = 0
while i < num_subjects :
    print("Yo estudie la materia de",subjects_list[i],'y he sacado', score_list[j]) 
    i +=1
    j +=1
