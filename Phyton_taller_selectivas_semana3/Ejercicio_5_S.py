"""
Entradas:
importeglobal--->float--->img
sueldobase--->float--->sb
venta1--->float--->v1
venta2--->float--->v2
venta3--->float--->v3
Salidas:
sueldo1--->float--->s1
sueldo2--->float--->s2
sueldo3--->float--->s3
"""
img=float(input ("Importe global: "))
sb=float(input("Sueldo basico: "))
v1=float(input("Insertar el valor de ventas del departamento 1: "))
v2=float(input("Insertar el valor de ventas del departamento 2: "))
v3=float(input("Insertar el valor de ventas del departamento 3: "))
p1=((v1*100)/img)
p2=((v2*100)/img)
p3=((v3*100)/img)
stotal=(sb+(sb*0.2))
if(p1>33):
  print("Salario del vendedor 1: "+str(stotal))
else:
  print("Sueldo vendedor 1: "+str(sb))
if(p2>33):
  print("Salario vendedor 2: "+str(stotal))
else:
  print("Sueldo vendedor 2: "+str(sb))
if(p3>33):
  print("Salario vendedor 3: "+str(stotal))
else:
  print("Sueldo vendedor 3: "+str(sb))
  