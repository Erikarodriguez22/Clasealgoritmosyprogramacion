"""
Entradas:
valorp-->int-->P
valorq-->int-->Q
Salidas:
Expresión-->int-->expr

"""
P=int(input("Inserte valor de P: "))
Q=int(input("Inserte valor de Q: "))
expr=(P*P*P)+(Q*Q)-(2*(P*P))
if (expr<=680):
    print("P y Q satisfacen la expresión")
else:
    print("P y Q no satisfacen la expresión")

