"""
Entradas:
Nombre--->str--->nombre
montocompra--->float--->moncomp
Salidas:
montoapagar--->float--->total
descuento--->float--->desc
"""
nombre=str(input("Nombre del cliente: "))
moncomp=float(input("Monto de la compra: "))
if(moncomp>0 and moncomp<=50000):
  total=(moncomp-(moncomp*0.05))
  desc=(moncomp-total)
  print("Nombre del cliente: "+str(nombre)+(" Monto de la compra: "+str(moncomp)+(" Descuento: ")+str(desc)+" Valor total: "+str(total)))
elif(moncomp>50000 and moncomp<=100000):
  total=(moncomp-(moncomp*0.11))
  desc=(moncomp-total)
  print("Nombre del cliente: "+str(nombre)+(" Monto de la compra: "+str(moncomp)+(" Descuento: ")+str(desc)+" Valor total: "+str(total)))
elif(moncomp>100000 and moncomp<=700000):
  total=(moncomp-(moncomp*0.18))
  desc=(moncomp-total)
  print("Nombre del cliente: "+str(nombre)+(" Monto de la compra: "+str(moncomp)+(" Descuento: ")+str(desc)+" Valor total: "+str(total)))
elif(moncomp>1500000):
  total=(moncomp-(moncomp*0.25))
  desc=(moncomp-total)
  print("Nombre del cliente: "+str(nombre)+(" Monto de la compra: "+str(moncomp)+(" Descuento: ")+str(desc)+" Valor total: "+str(total)))