"""
Entradas:
precio de contado--->float--->P
valor de la cuota mensual--->float--->T
Salidas:
precio cuotas--->float--->precioc
recargo--->float--->recargo
porcentaje de recargo--->float--->porcentaje
"""
P=float(input ("Precio de contado:" ))
T=float(input ("Valor de la cuota mensual: "))
precioc=(T*12)
recargo=(precioc-P)
porcentaje=((recargo*100/P))
print("El porcentaje de recargo es: "+str(porcentaje), "%")