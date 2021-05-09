"""
Entradas:
K-->int
N-->int
Salidas:
kn-->int-->valork
"""
N=int(input("N= "))
K=int(input("K= "))
kn=N+1
while (N>K):
    lista=[]
    for i in range (K,kn):
        lista.append(i)
    lista.sort(reverse=True)
    print(lista)
    break
else:
    print("el valor de K debe ser menor de N")
    