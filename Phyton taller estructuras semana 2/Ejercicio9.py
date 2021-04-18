"""
Entradas:
Horas trabajadas--->float--->horast
precio--->float--->precio
Salidas:
Salario bruto--->float--->sbrut
descuentos--->float--->desc
salario neto--->float--->stotal
"""
horast=float(input("Ingrese el numero de horas trabajadas: "))
precio=float(input("Ingrese el valor por cada hora de trabajo: "))
sbrut=(horast*precio)
desc=(sbrut*0.2)
stotal=(sbrut-desc)
print("El salario total es: "+str(stotal))