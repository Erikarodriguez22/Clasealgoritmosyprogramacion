"""
Entradas:
MATEMATICAS
Examen matem--->float--->matex
tarea 1--->float--->mat1
tarea 2--->float--->mat2
tarea 3--->float--->mat3
FISICA
examen fisica--->float--->fiex
tarea 1--->float--->fi1
tarea 2--->float--->fi2
QUIMICA
examen quimica--->float--->quimex
tarea 1--->float--->quim1
tarea 2--->float--->quim2
tarea 3--->float--->quim3
Salidas:
Promedio matematicas--->float--->avmat
promedio fisica--->float--->avfi
promedio quimica--->float--->avquim
promedio general--->float-promedio
"""
print("MATEMATICAS: ")
matex=float(input("Nota del examen: "))
mat1=float(input("Nota de la tarea 1: "))
mat2=float(input("Nota de la tarea 2: "))
mat3=float(input("Nota de la tarea 3: "))
avmat=(matex*0.9)+(((mat1+mat2+mat3)/3)*0.1)
print("FISICA: ")
fiex=float(input("Nota del examen: "))
fi1=float(input("Nota de la tarea 1: "))
fi2=float(input("Nota de la tarea 2: "))
avfi=(fiex*0.8)+(((fi1+fi2)/2)*0.2)
print("QUIMICA: ")
quimex=float(input("Nota del examen: "))
quim1=float(input("Nota de la tarea 1: "))
quim2=float(input("Nota de la tarea 2: "))
quim3=float(input("Nota de la tarea 3: "))
avquim=(quimex*0.85)+(((quim1+quim2+quim3)/3)*0.15)
promedio=((avmat+avfi+avquim)/3)
print("PROMEDIO MATEMATICAS: "+str(avmat))
print("PROMEDIO FISICA: "+str(avfi))
print("PROMEDIO QUIMICA: "+str(avquim))
print("PROMEDIO GENERAL: "+str(promedio))