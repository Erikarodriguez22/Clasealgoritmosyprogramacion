"""
Entradas:
Ladoa-->float-->a
ladob-->float-->b
ladoc-->float-->c
salidas:
semiperimetro-->float-->S
area-->float-->A
"""
a=float(input("Insertar valor de lado a: "))
b=float(input("Insertar valor de lado b: "))
c=float(input("Insertar valor de lado c: "))
S=((a+b+c)/2)
A=((S*(S-a)*(S-b)*(S-c))**0.5)
print("El area del triangulo es: "+str(A))