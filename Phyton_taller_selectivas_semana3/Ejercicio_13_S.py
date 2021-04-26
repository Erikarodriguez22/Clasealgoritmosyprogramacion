"""
Entradas:
dia-->int-->dia
mes-->int-->mes
año-->int-->año
Salidas:
Signo-->str-->signo
edad-->str-->edad
"""
dia=int(input("Ingrese el día de nacimiento: "))
mes=int(input("Ingrese el mes de nacimiento: "))
año=int(input("Ingrese el año de nacimiento: "))
if((mes==11) and (dia>=22)) or ((mes==12) and (dia<=21)):
    print("El signo es Sagitario")
if((mes==12) and (dia>=22)) or ((mes==1) and (dia<=20)):
    print("El signo es Capricornio")
if((mes==1) and (dia>=21)) or ((mes==2) and (dia<=19)):
    print("El signo es Acuario")
if((mes==2) and (dia>=20)) or ((mes==3) and (dia<=19)):
    print("El signo es Psicis")
if((mes==3) and (dia>=21)) or ((mes==4) and (dia<=20)):
    print("El signo es Aries")
if((mes==4) and (dia>=21)) or ((mes==5) and (dia<=21)):
    print("El signo es Tauro")  
if((mes==5) and (dia>=22)) or ((mes==6) and (dia<=21)):
    print("El signo es Geminis")
if((mes==6) and (dia>=22)) or ((mes==7) and (dia<=22)):
    print("El signo es Cancer")
if((mes==7) and (dia>=23)) or ((mes==8) and (dia<=23)):
    print("El signo es Leo")
if((mes==8) and (dia>=24)) or ((mes==9) and (dia<=22)):
    print("El signo es Virgo")
if((mes==9) and (dia>=23)) or ((mes==10) and (dia<=22)):
    print("El signo es Libra")
if((mes==10) and (dia>=23)) or ((mes==11) and (dia<=21)):
    print("El signo es Escorpion")

from datetime import datetime
from dateutil.relativedelta import relativedelta
nacim=(str(dia)+("/")+str(mes)+("/")+str(año))
fecha_nacimiento= datetime.strptime(nacim, "%d/%m/%Y")
edad= relativedelta(datetime.now(), fecha_nacimiento)
print(f"{edad.years} años, {edad.months} meses y {edad.days} días")

