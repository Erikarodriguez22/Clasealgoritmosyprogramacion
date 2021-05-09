dividendo=int(input("Ingresar dividendo: "))
divisor=int(input("Ingresar divisor: "))
if dividendo>0 and divisor>0:
    cociente=0
    residuo=dividendo
    while(residuo>=divisor):
        residuo-=divisor
        cociente+=1
print(residuo)
print(cociente)

