"""
Entradas
Chelines--->float--->CHA
Dracmas--->float-DRG
Pesetas--->float--->PST
Salidas
Pesetas--->float---PST
Francos Franceses--->float--->FRA
dolares--->float--->USD
Liras--->float--->LIR
"""
print("Chelines a Pesetas: ")
CHA=float(input("Ingrese el valor en chelines: "))
PST=((CHA*956871)/100)
print("El valor en pesetas es: "+str(PST))
print("Dracmas a francos: ")
DRA=float(input("Ingrese el valor en dracmas: "))
PST=((DRA*88607)/100)
FRA=(PST/20110)
print("El valor en francos es: "+str(FRA))
print("Pesetas a dolares y liras italianas: ")
PST=float(input("Escriba el valor en pesetas: "))
USD=(PST/122499)
LIR=((PST*100)/9289)
print("El valor en dolares es: "+str(USD))
print("El valor en liras es: "+str(LIR))