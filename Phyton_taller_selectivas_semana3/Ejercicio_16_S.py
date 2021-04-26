"""
Entradas:
valora-->int-->A
valorb-->int-->B
valorc-->int--->C
Valord-->int-->D
Salidas:
x1-->float-->1x
x2-->float-->2x
"""
A=int(input("Inserte el valor de A: "))
B=int(input("Inserte el valor de B: "))
C=int(input("Inserte el valor de C: "))
D=((B**2)-4*A*C)
if(D==0):
  x=(-B/2*A)
  print("La solución única es:"+str(x))
elif(D>0):
  x=((-B)+((B**2-(4*A*C))/(2*A))**0.5)
  z=((-B)-((B**2-(4*A*C))/(2*A))**0.5)
  print("Las dos soluciones reales son: X1:"+str(x),("X2")+str(z))
elif(D<0):
    print("No tiene solución en los reales")

