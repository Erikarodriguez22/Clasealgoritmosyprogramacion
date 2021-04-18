"""
Entradas:
nombre--->str--->nombre
horas normales trabajadas--->float--->horasnt
valor hora normal--->float--->valorhn
horas extra trabajadas--->float--->horaset
numero hijos--->int--->hijos
Salidas:
valor horas trabajadas--->float--->pht
precio hora extra trabajada--->float--->phet
sueldo base--->float--->sbase
deducciones--->float-deducciones
asignaciones--->float--->asig
sueldo neto--->float--->stotal
"""
nombre=str(input("Nombre del trabajador: "))
horasnt=float(input("Horas normales trabajadas: "))
valorhn=float(input("Valor de la hora normal: "))
horaset=float(input("Horas extra trabajadas: "))
pht=(horasnt*valorhn)
phet=(horaset*(valorhn*1.25))
sbase=(phet+pht)
deducciones=(sbase*0.14)
print("Sueldo base: "+str(sbase))
print("Total deducciones: "+str(deducciones))
hijos=int(input("Numero de hijos del trabajador: "))
asig=(250000+(hijos*173000)+180000)
print("Total asignaciones: "+str(asig))
stotal=(sbase+asig-deducciones)
print("El sueldo neto es: "+str(stotal))