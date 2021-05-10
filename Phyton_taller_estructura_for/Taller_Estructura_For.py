archivo = open('paises.txt', 'r')

#Imprimir lista
"""
for pais_y_capital in archivo:
 print(pais_y_capital)
"""
#imprima la posicion de colombia
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="Colombia: Bogotá\n"):
    break
  lista=[]   
print(c)
"""
#Imprima todos los paises
"""
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
"""
#Imprima todas las Capitales
"""
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
"""  
#Imprimir todos los paises que inicien con la letra C
"""
lista=[]
paises=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
for i in paises:
  if(i[0]=="C"):
    print(i)
"""
#imprima todas las capitales que inicien con la leta B
"""
lista=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:
  if(i[0]=="B"):
    print(i)  
"""
#Cuente e imprima cuantas ciudades inician con la latra M
"""
lista=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:
  if(i[0]=="M"):
    print(i)
    lista.append(i)
print(len(lista))
"""
#Imprima todos los paises y capitales, cuyo inicio sea con la letra U

"""
lista=[]
pais_y_capital=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  pais_y_capital.append(a)
  lista=[]
for i in pais_y_capital:
  if(i[0]=="U"):
    print(i)
lista=[]
pais_y_capital=[]  
for i in archivo:
    b=i.index(":")
    for r in range(b+2,len(i)):
      lista.append(i[r])
      b="".join(lista)
      pais_y_capital.append(b)
lista=[]
for i in pais_y_capital:
  if(i[0]=="U"):
   print(i) 


"""

#Cuente e imprima cuantos paises que hay en el archivo

"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a="".join(lista)
  c=c+1
print(len(lista))

"""

#Busque e imprima la ciudad de Singapur

"""
palabra="Singapur: Singapur"
b=palabra.index(":")
tamaño=len(palabra)
lista=[]
for i in range(b+1,tamaño):
    lista.append(palabra[i])
unir="".join(lista)
print(unir)
"""
#Busque e imprima el pais de Venezuela y su capital
"""
palabra="Venezuela: Caracas"
b=palabra.index(":")
tamaño=len(palabra)
lista=[]
for i in range(0,18):
    lista.append(palabra[i])
unir="".join(lista)
print(unir)
"""
#Cuente e imprima las ciudades que su pais inicie con la letra E

"""
lista=[]
paises=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
for i in paises:
  if(i[0]=="E"):
   print(i)
   lista.append(i)
print(len(lista))
"""

#Buesque e imprima la Capiltal de Colombia
"""
palabra="Colombia: Bogotá"
b=palabra.index(":")
tamaño=len(palabra)
lista=[]
for i in range(b+1,tamaño):
    lista.append(palabra[i])
unir="".join(lista)
print(unir)
"""

#imprima la posicion del pais de Uganda
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="Uganda: Kampala\n"):
    break
  lista=[]   
print(c)
"""
#imprima la posicion del pais de Mexico
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="México: Ciudad de México \n"):
    break
  lista=[]   
print(c)
"""
"""
El alcalde de Antananarivo contrato a algunos alumnos de la Universidad Ean para corregir el archivo de países.txt, ya que la capital de Madagascar NO es rey julien es Antananarivo, espero que el alcalde se vaya contento por su trabajo. Utilice un For para cambiar ese Dato
"""
"""
lista=[]
for pais_y_capital in archivo:
 pais_y_capital.remove=("Madagascar: rey julien")
 lista.insert=(149,"Madagascar: Antananarivo")
 print(pais_y_capital)
"""
#Agregue un país que no esté en la lista 
"""
lista=[]
pais_y_capital=[]
for pais_y_capital in archivo:
    lista.insert(149,"Qatar:Doha")
    print(pais_y_capital)
"""

"""
archivo.close()
"""