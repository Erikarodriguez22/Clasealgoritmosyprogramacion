"""
Entradas:
Numeropiezas--->int--->npiezas
Preciounitario--->float--->precio
Salidas: 
Valorcompra--->float--->valorc
dineropropio--->float-->propio
creditobanco--->float--->cred
creditofabricante--->fab
interes-->float--->interes
"""
npiezas=int(input ("Numero de piezas compradas: "))
precio=float(input ("Valor de cada pieza: "))
valorc=(npiezas*precio)
if(valorc<=5000000):
  propio=(valorc*0.7)
  fab=(valorc*0.3)
  interes=(fab*0.2)
  print("Valor a pagar con el dinero de la empresa es: "+str(propio))
  print("Valor del credito: "+str(fab))
  print("Valor del interes: "+str(interes))
else:
  propio=(valorc*0.55)
  fab=(valorc*0.15)
  interes=(fab*0.2)
  cred=(valorc*0.3)
  print("Valor a pagar con dinero de la empresa: "+str(propio))
  print("Valor del credito: "+str(fab))
  print("Valor del interes: "+str(interes))
  print("El monto a solicitar al banco es: "+str(cred))
  