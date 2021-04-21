"""
Entradas:
precio final--->float--->pfin
precio de venta--->float--->pventap
Salidas:
diferencia--->float--->dif
porcentaje descuento--->float--->desc
"""
pfin=float(input ("Digite el valor pagado: "))
pventp=float(input ("Ingrese el precio de venta sugerido: "))
dif=(pventp-pfin)
desc=((dif*100)/pventp)
print("El porcentaje de descuento fue: "+str(desc))