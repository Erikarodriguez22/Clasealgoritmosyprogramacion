"""
Entradas:
venta en galones--->float--->gal
Salidas
venta en litros--->float--->lts
total venta--->float--->total
"""
gal=float(input ("Ingrese la venta en galones: "))
lts=(gal*3.785)
total=(lts*50000)
print("El total de la venta es: "+str(total))