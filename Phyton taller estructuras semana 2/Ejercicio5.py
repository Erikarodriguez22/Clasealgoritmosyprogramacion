"""
Entradas
Parcial1-->float-->P1
Parcial2-->float-->P2
Parcial3-->float-->P3
Examenfinal-->float-->Ef
Trabajofinal-->float-->Tf
Salidas
Promedioparciales-->float-->Promp
Notadefinitiva-->float-->Notafinal
"""
P1=float(input("Nota del parcial 1: "))
P2=float(input("Nota del parcial 2: "))
P3=float(input("Nota del parcial 3: "))
Ef=float(input("Nota examen final: "))
Tf=float(input("Nota del trabajo final: "))
Promp=((P1+P2+P3)/3)
Notafinal=((Promp*0.55)+(Ef*0.33)+(Tf*0.15))
print("Nota definitiva: "+str(Notafinal))
