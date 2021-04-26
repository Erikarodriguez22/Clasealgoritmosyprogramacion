"""
Entradas:
edad-->int-->edad
hemoglobina-->float-->nivhem
sexo-->int--->sexo
Salidas:
positivoonegativo para anemia-->str
mujerohombre-->str
"""
edad=int(input("Ingresar el valor de edad en meses:"))
nivhem=float(input("Ingresa el valor de nivel de hemoglobina:"))
sexo=int(input("Ingrese su sexo (F)=1 (M)=0: "))
if(sexo==1):
 print("Mujer")
else:
 print("Hombre")

if (edad>0 and edad<=1 and nivhem<13):
    print("Positivo para anemia")
elif (edad>1 and edad<=6 and nivhem<10):
    print("Positivo para anemia")
elif (edad>6 and edad<=12 and nivhem<11):
    print("Positivo para anemia")
elif (edad>12 and edad<=60 and nivhem<11.5):
    print("Positivo para anemia")
elif (edad>60 and edad<=120 and nivhem<12.6):
    print("Positivo para anemia")
elif (edad>120 and edad<=180 and nivhem<13):
    print("Positivo para anemia")
elif (edad>180 and sexo==1 and nivhem<12):
    print("Mujer positiva para anemia")
elif (edad>180 and sexo==0 and nivhem<14):
    print("Hombre positivo para anemia")
else:
    print("Negativo para anemia")

