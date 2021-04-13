Algoritmo Inicio_Conversiondetiempo
	Escribir "Convertidor de minutos a horas"
	Escribir "Numero de minutos: "
	Leer Minutos
	Minutossobran<-Minutos%60
	Escribir (Minutos-Minutossobran)/60, " Horas ",minutossobran, " Minutos "	
FinAlgoritmo