"""
Entradas:
Salariobruti-->float--> sb
Salidas:
salarioneto-->float Sn
"""
sb=float(input("Salario bruto: "))
if(sb<900000):
 sn=sb+(sb*0.15)
 print("El salario neto es: "+str(sn))

else:
    sn=sb+(sb*0.12)
    print("El salario neto es: "+str(sn))
    
