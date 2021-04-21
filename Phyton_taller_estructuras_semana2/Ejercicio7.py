"""
Entradas
Metros-->int-->Metros
Salidas
Pulgadas-->int-->Pulgadas
Pies-->int-->Pies
"""
Metros=int(input("Insertar valor en metros: "))
Pulgadas=(Metros*39.27)
Pies=(Pulgadas*12)
print("Metros a pulgadas: "+str(Pulgadas), "Metros a pies: "+str(Pies))