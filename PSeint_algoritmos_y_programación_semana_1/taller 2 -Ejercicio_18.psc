Algoritmo Inicio_porcentaje
	Escribir "Insertar capital: "
	Leer Cap
	Escribir "Insertar la tasa de interes: "
	Leer Tasa
	Escribir "Insertar el tiempo de inversi�n: "
	Leer Tiempo
	Interes<-((Cap*Tasa*Tiempo)/100)
	prom<-(Interes*1/Tiempo)
	Escribir "El interes es: ", Interes
	Escribir "Promedio anual de intereses: ",prom, "%"
FinAlgoritmo
