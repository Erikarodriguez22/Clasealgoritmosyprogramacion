"""
Entradas:
cantidad de naranjas--->int--->X
precio por docena--->float--->Y
valor venta--->float--->K
Salidas:
numero de docenas--->float--->docena
costo--->float--->precio
ganancia--->float--->ganancia
porcentaje ganancia--->float--->porcentaje
"""
X=int(input ("Numero de naranjas: "))
Y=float(input ("Valor por docena: "))
K=float(input ("Valor de las ventas: "))
docena=(X/12)
precio=(Y*docena)
ganancia=(K-precio)
porcentaje=((ganancia*100)/precio)
print("El porcentaje de ganancias es: "+str(porcentaje), "%")