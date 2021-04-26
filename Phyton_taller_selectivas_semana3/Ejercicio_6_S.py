"""
Entradas:
ValorA-->int-->A
ValorB-->int-->B
ValorC-->int-->C
ValorD-->int-->D
Salidas:
valor-->int
"""
A=int(input("Valor de A: ")) 
B=int(input("Valor de B: "))
C=int(input("Valor de C: "))
D=int(input("Valor de D: "))
if(C>5):
  C=0
  D=0
  B=B+1
elif(C<5):
  #2442
  C=0
  D=0
elif(C==5):
  #2451
  D=0
N1=A
N2=B
N3=C
N4=D

print("El valor aproximado es: "+str(N1)+str(N2)+str(N3)+str(N4))

