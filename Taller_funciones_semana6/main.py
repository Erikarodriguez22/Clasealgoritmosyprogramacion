frutas = open('frutas.txt', 'r')
numeros= open('numeros.txt','r')
lista_frutas=[]#Llenar las lista con los datos del archivo frutas.txt
lista_numeros=[]#Llenar las lista con los datos del archivo numeros.txt
for i in frutas:
    lista_frutas.append(i)
print(lista_frutas)
for i in numeros:
    lista_numeros.append(float(i))
print(lista_numeros)

#Realizar una funcion que elimine un caracter de todos los elementos de la lista
"""
Entradas:
lista-->list-->lista

Salidas:
lista-->lista
"""

def eliminar_un_caracter_de_toda_la_lista(lista,elemento):
    auxiliar=[]
    for i in lista:
     a=i.replace(elemento,"")
     auxiliar.append(a)
    return auxiliar

 

#Realizar una funcion que retorne la copia de una funcion que pasa por parametro 
"""
Entradas:
lista->list-->lista
Salidas:
lista->list-->lista
"""

def copia_lista(lista):
    aux=[]
    for i in lista:
        aux.append(i)
    return aux


#Realizar una funcion que retorne una lista de numeros enteros   
"""
Entradas:
lista-list-->lista
Salidas
lista-list-->lista
"""  
def numeros_pares(lista):
  aux=[]
  for i in lista:
    if(float(i)%2==0):
      aux.append(i)
  return aux 


#Realizar una funcion que elimine un elemento de una lista
"""
Entradas:
lista-list-->lista
elemento-->str-->elemento
Salidas
lista-list-->lista
"""  
def elimina_elemento_lista(lista,elemento):
  lista.remove(elemento)
  return lista


#Retorna una lista con las palabras iniciales con la letra que pasa por parametro  
"""
Entradas:
lista-list-->lista
Salidas
lista-list-->lista

"""  

def letra(lista):
    aux=[]
    for i in lista:
        aux.append(i)
    return aux

#Realizar una funcion que retorne el tamaño de una lista   
"""
Entradas:
Lista->list-->lista
Salidas
tamaño lista
"""   

def tamano_lista(lista):
    contador=0
    while True:
        try:
            lista[contador]
            contador +=1
        except IndexError:
            break
    return


#Retorna el tamaño de la lista y que tipo de datos estan dentro de la lista
"""
Entradas:
lista-->list-->lista
Salidas
lista-->lista
tipodatos
"""  

def informacion_lista(lista):
  contador=0
  while True:
        try:
            lista[contador]
            contador +=1
        except IndexError:
            break
  return

#Retornar una lista con los numero negativos  
"""
Entradas:
Salidas
"""  

def numeros_negativos(lista):
  for i in lista:
   c = 0 
   for numeros in lista:
       if numeros <= 0:
           c += 1 
   return c

#realizar una funcion que retorne la posicion de un elemento que pasa por parametro

"""
def posicion_elemento(elemento):
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
#realizar una funcion que agregue al final de archivo frutas una fruta
"""
def frutas(elemento):
    lista.insert(45,"elemento")
    print(lista_frutas)

"""
#Realizar una funcion que cuente el numero de veces que se repite un elemento  

def contar_veces(self, elemento, lista):
    veces = 0
    for i in lista:
         if elemento==i:
             veces += 1
    return veces

"""
if __name__ == "__main__":
    nueva=eliminar_un_caracter(lista_numeros,"\n")
    nueva_dos=numeros_pares(nueva)
    print(elimina_elemento_lista(nueva_dos,"10"))
"""
