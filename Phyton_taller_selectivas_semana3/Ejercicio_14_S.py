"""
Entradas:
Lecturactual-->float-->act
Lecturaanterior-->float-->ant
Salidas:
valorfactura-->float-->total
"""
act=float(input("Lectura actual: "))
ant=float(input("Lectura anterior: "))
consumo=(act-ant)
if(consumo>=0 and consumo<=100):
 total=(consumo*4600)
 print("Monto a pagar: "+str(total))
elif(consumo>=101 and consumo<=300):
 total=(consumo*80000)
 print("Monto a pagar: "+str(total))
elif(consumo>=301 and consumo<=500):
 total=(consumo*100000)
 print("Monto a pagar: "+str(total))
elif(consumo>=501):
 total=(consumo*120000)
 print("Monto a pagar: "+str(total))
