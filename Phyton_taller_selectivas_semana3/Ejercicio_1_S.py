"""
Entradas:
Cantidadinvertida-->float-->cap
Tasainteres--->float--->tin
Salidas:
Ganancia--->float--->gan
gananciaconinversion--->float--->total
"""
cap=float(input("Capital invertido: "))
tin=float(input ("Tasa de interes: "))
gan=cap*(tin/100)
total=((gan+cap)*tin)
if(gan<100000):
  print("El valor de las ganancias es: "+str(gan))
else:
  print("El valor total en la cuenta será: "+str(total))

  