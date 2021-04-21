Algoritmo Inicio_Notafinal
	Escribir "Calculo nota algoritmos y programacion"
	Escribir "Nota primer parcial: "
	Leer Parcial1
	Escribir "Nota segundo parcial: "
	Leer Parcial2
	Escribir "Nota tercer parcial: "
	Leer Parcial3 
	Promedioparciales<-((Parcial1+Parcial2+Parcial3)/3)
	Escribir "Promedio Parciales: ", Promedioparciales
	Escribir "Nota examen final: "
	Leer Examenfinal
	Escribir "Nota trabajo final: "
	leer Trabajofinal
	Escribir "Nota definitiva: ", ((Promedioparciales*0.55)+(Examenfinal*0.3)+(Trabajofinal*0.15))
FinAlgoritmo
