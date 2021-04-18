"""
Entradas
Venta-->float-->Venta
Salidas
Descuento-->float-->D
Valor total-->float-->total
"""
Venta=float(input("Digite la venta: "))
D=(Venta*0.15)
total=(Venta-D)
print("valor de descuento: "+str(D)," valor a pagar: "+str(total))