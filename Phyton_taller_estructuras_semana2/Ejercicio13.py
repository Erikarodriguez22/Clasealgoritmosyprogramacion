"""
Entradas:
N1--->int-->V1
N2--->int-->V2
N3--->int-->V3
N4--->int-->V4
N5--->int-->V5
N6--->int-->V6
N7--->int-->V7
N8--->int-->V8
Salidas:
Dinero total en el banco--->int--->total
"""
V1=int (input ("Numero de billetes de $50.000: "))
V2=int (input ("Numero de billetes de $20.000: "))
V3=int (input ("Numero de billetes de $10.000: "))
V4=int (input ("Numero de billetes de $5.000: "))
V5=int (input ("Numero de billetes de $2.000: "))
V6=int (input ("Numero de billetes de $1.000: "))
V7=int (input ("Numero de billetes de $500: "))
V8=int (input ("Numero de billetes de $100: "))
total=((V1*50000)+(V2*20000)+(V3*10000)+(V4*5000)+(V5*2000)+(V6*1000)+(V7*500)+(V8*100))
print("La cantidad de dinero en el banco es: " +str(total))