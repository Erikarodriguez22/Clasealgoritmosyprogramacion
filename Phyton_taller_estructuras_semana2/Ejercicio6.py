"""
Entradas
Mujeres-->int-->Mujeres
Hombres-->int-->Hombres
Salidas
Total-->int-->Total
"""
Mujeres=int(input("Numero de mujeres: "))
Hombres=int(input("Numero de hombres: "))
Total=(Mujeres+Hombres)
PorMuj=(Mujeres/Total*100)
PorHom=(Hombres/Total*100)
print("Porcentaje de mujeres: "+str(PorMuj), "Porcentaje de de hombres: "+str(PorHom))