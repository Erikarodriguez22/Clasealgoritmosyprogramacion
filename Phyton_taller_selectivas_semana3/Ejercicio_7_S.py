"""
Entradas:
kmrecorridos-->float-->km
Salidas:
Tarifa-->float-->valor
"""
km=float(input("Insertar la distancia recorrida en Km: "))
if(km<=300 and km>0):
  valor=50000
  print(" La tarifa es: "+str(valor))
elif(km>300 and km<=1000):
  valor=(70000+((km-300)*30000))
  print("La tarifa es: "+str(valor))
if(km>1000):
  valor=(150000+((km-1000)*9000))
  print("La tarifa es: "+str(valor))
  