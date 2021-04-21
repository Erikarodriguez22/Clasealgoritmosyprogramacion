Algoritmo Inicio_porcentajerecargo
	Escribir "Precio de contado: "
	Leer P
	Escribir "Valor cuota mensual: "
	Leer T
	Preciocontado<-(T*12)
	Recargo<-(Preciocontado-P)
	Porcentaje<-((Recargo*100)/P)
	Escribir " El porcentaje de recaudo en el precio es: ", Porcentaje "%"
	FinAlgoritmo
