"""
Entradas:
categoria--->int--->cat
salario--->float--->sal
Salidas:
aumento--->float--->au-nsb
"""
cat=int(input("Inserte la categoria: "))
sal=float(input("Inserte el salario bruto: "))
if(sal>4300000 and sal<=5000000):
  au=(sal+(sal*0.10))
  ncat=(1)
  print("Categoria: "+str(ncat)+(" Nuevo salario bruto: "+str(au)))
if(sal>3600000 and sal<=4300000):
  au=(sal+(sal*0.15))
  ncat=(2)
  print("Categoria: "+str(ncat)+(" Nuevo salario bruto: "+str(au)))
if(sal>2000000 and sal<=3600000):
  au=(sal+(sal*0.2))
  ncat=(3)
  print("Categoria: "+str(ncat)+(" Nuevo salario bruto: "+str(au)))
if(sal>900000 and sal<=2000000):
  au=(sal+(sal*0.4))
  ncat=(4)
  print("Categoria: "+str(ncat)+(" Nuevo salario bruto: "+str(au)))
if(sal>0 and sal<=900000):
  au=(sal+(sal*0.4))
  ncat=(5)
  print("Categoria: "+str(ncat)+(" Nuevo salario bruto: "+str(au)))
  

