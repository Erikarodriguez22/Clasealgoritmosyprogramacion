Proceso Ejercicio_Descuento
	Escribir "Digite el precio pagado por el artículo:"
	Leer pfinal
	Escribir "Digite el precio de venta al público:"
	Leer pventap
	dif<-(pventap-pfinal)
	desc<-((dif*100)/pventap)
	Escribir "El descuento aplicado fue: ",desc,"%"
FinProceso
