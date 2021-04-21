Algoritmo Inicio_porcentajeganancia
	Escribir "Cantidad de naranjas"
	Leer X
	Docena<-(X/12)
	Escribir "Valor de la docena: "
	Leer I
	Precio<-(I*Docena)
	Escribir "Valor de la venta: "
	Leer K
	Ganancia<- (K-Precio)
	Porcentaje<-((Ganancia*100)/Precio)
	Escribir "Porcentaje de ganancia: ", Porcentaje "%"
	FinAlgoritmo
