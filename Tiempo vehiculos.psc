Algoritmo Inicio_Tiempovehiculos
	Escribir "Tiempo en el que el vehiculo 2 alcanza al 1"
	Escribir "Distancia enre los dos vehiculos en Km:"
	Leer Distancia
	Escribir "Velocidad vehiculo 1 en Km/h: "
	Leer V1
	Escribir "Velocidad vehiculo 2 en Km/h: "
	Leer V2
	Diferenciavel<-(V2-V1)
	Tiempoh<-(Distancia/Diferenciavel)
	Tiempominutos<-(Tiempoh+60)
	Escribir "El vehiculo 2 alcanza al vehiculo 1 en: ", Tiempominutos, "minutos"
FinAlgoritmo
