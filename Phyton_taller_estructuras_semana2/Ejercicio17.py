"""
Entradas:
Presupuesto total--->float--->presup
Salidas:
presupuesto ginecologia--->float--->ginecologia
presupuesto traumatologia--->float--->traumatologia
presupuesto pediatria--->float--->pediatria
"""
presup=float(input ("Digite el valor del presupuesto total anual "))
ginecologia=(presup*0.4)
traumatologia=(presup*0.3)
pediatria=(presup*0.3)
print("El presupuesto de ginecologia es: "+str(ginecologia))
print("El presupuesto de traumatologia es: "+str(traumatologia))
print("El presupuesto de pediatria es: "+str(pediatria))