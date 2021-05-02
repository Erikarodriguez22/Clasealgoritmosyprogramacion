""""
Entradas:
Nombre-->str-->n
Numerocedula-->int-->cd
tipodevehiculo-->int-->tipo
Registroplaca-->str-->placa
Salida:
valorapagar-->int-->vpag
tipoparqueadero-->int-->tipo
valorapagarcondescuento-->desc
lugardeparqueo-->int-->parqueo
"""

print("¡¡BIENVENIDO AL PARQUEADERO DE LA UNIVERSIDAD EAN!! 🥳 🤓")

usuario=int(input("Si eres empleado del parqueadero ingresa 1 si eres usuario 0:"))
if(usuario==1):
 empleado=(input("Digite Usuario: "))
 contraseña=((input("Digite contraseña:")))
 lista=["erika","1234"]
 while True:
  empleado=input("Digite Usuario: ")
  contraseña=input("Digite contraseña: ")
  if(empleado==lista[0]):
   if(contraseña==lista[1]):
     print("Bienvenido 🎉")
  break
#Validación........................................
if(usuario==0):     
 n=input("Ingrese su nombre completo: ")
#Validación...................................................
 while True:
   cd=input("Ingrese su número de cédula: ")
   try:
     cd=int(cd)
     if(cd>0):
        break
     else:
        print("El número de cedula debe ser positivo⚠️")  
   except:
    print("Ingrese solo numero su cédula ⚠️")
#----------------------------------------------------     
 while True:
    tipo=input("1-->para carro 🚗, 2-->para moto 🏍️, 3-->para bicicleta🚲: ")
    try:
     tipo=int(tipo)  
     if(tipo==1 or tipo==2 or tipo==3):
       break
     else:
        print("Número fuera del rango, ingrese un número nuevamente ⚠️")
    except:
       print("Ingrese solo números del 1 al 3")

 if(tipo==1 or tipo==2):
     placa=(input("Ingrese placa: "))
     print(placa[0],placa[1],placa[2])
     print(placa[3],placa[4],placa[5])

 else:
     registro=(input("Ingrese número de registro: "))
     print(registro[0],registro[1],registro[2])
     print(registro[3],registro[4],registro[5])
     print(registro[6],registro[7])

#carro: 3 letras y 3 números
#moto: 3 letras y 3 números
#moto: 3 letras 2 números 
#Moto: 3letras 2 números 1 letra
#bicicletas: 8 numeros

import time

#tiempo entrada carro
tiempo1_min=time.gmtime()
he=(tiempo1_min[3]*60)
me=tiempo1_min[4]
he_min=me+he

#ingreso
localtime=time.asctime( time.localtime(time.time()))
print("Hora ingreso 🕐  :", localtime)


cc=int(input("Ingrese su CC para saber si cuenta con un descuento 🤑  💲: "))
listaCc=[1019134469,1019134469,1019134469,1019134469]
listaCc.append(cc)
#cuentas cedulas hayprint(listaCc.count(cc))
if(listaCc.count(cc)==5):
  print("tiene descuento del 20% por su fidelidad 💲",cc)
else:
  print("no tine descuento♦️: ",cc)  


"""
#Lugar para parquear:
parqueo=("Ingrese el piso en el que desea parquear:")
listaparp1c=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,160]

listaparp1c.append()

listaparqp1m=[161,162,163,164,165,166,167,168,169,170]
listaparqp1m.append()
listaparp1b=[171,172,173,174,175,176,177,178,179,180]
listaparqp1b.append()

listaparqueop2c=[201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260]
listaparqueop2m=[261,262,263,264,265,266,267,268,269,270]
listaparqueop2b=[271,272,273,274,275,276,277,278,279,280]

listaparqueop3=[301,302,303],304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354,355,356,357,358,359,360]
listaparqueop3m=[361,362,363,364,365,366,367,368,369,370]
listaparqueop3b=[371,372,373,374,375,376,377,378,379,380]

"""


#Total a pagar  
import time
tiempo2_min=time.gmtime()
hs=(tiempo2_min[3]*60)
ms=tiempo2_min[4]
hs_min=me+he
x=hs-he
if(x<0):
  if(listaCc.count(cc)==5):
   if(tipo==1):
     tp=he_min*100-(he_min*100*0.2)
     print("Total a pagar "+str(tp)+" COP")
   elif(tipo==2):
     tp=he_min*70-(he_min*70*0.2)
     print("Total a pagar "+str(tp)+" COP")
   else:
     tp=he_min*60-(he_min*60*0.2)
     print("Total a pagar "+str(tp)+" COP")
  else:
      if(tipo==1):
       tp=he_min*100
       print("Total a pagar "+str(tp)+" COP")
      elif(tipo==2):  
        tp=he_min*70
        print("Total a pagar "+str(tp)+" COP")
      else:
       tp=he_min*60
       print("Total a pagar "+str(tp)+" COP")
else:
    if(listaCc.count(cc)==5):
      if(tipo==1):
        tp=(hs_min-he_min)*100-((hs_min-he_min)*100*0.2)
        print("Total a pagar "+str(tp)+" COP")
      elif(tipo==2):
       tp=(hs_min-he_min)*70-((hs_min-he_min)*70*0.2)
       print("Total a pagar "+str(tp)+" COP")
      else:
       tp=(hs_min-he_min)*60-((hs_min-he_min)*60*0.2)
       print("Total a pagar "+str(tp)+" COP")
    else:
      if(tipo==1):
       tp=(hs_min-he_min)*100
       print("Total a pagar "+str(tp)+" COP")
      elif(tipo==2):
       tp=(hs_min-he_min)*70
       print("Total a pagar "+str(tp)+" COP")
      else:
       tp=(hs_min-he_min)*60
       print("Total a pagar "+str(tp)+" COP")

print("Dirijase al cajero para realizar el pago💵 💸")
print("✨  Muchas gracias✨")

print("ESPERAMOS LE HAYA GUSTADO NUESTRO SERVICIO  🤝🏻")
print("¡¡¡VUELVA PRONTO!!!, FELIZ DÍA 🤗 😁 ")



