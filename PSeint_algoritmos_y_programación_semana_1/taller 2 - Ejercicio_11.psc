Proceso Ejercicio_Calculosalario
	Escribir "Itroduzca los siguientes datos: "
	Escribir "Nombre: "
	Leer nombre
	Escribir "Horas normales trabajadas: "
	Leer horasnt
	Escribir "Valor de la hora normal: "
	Leer valorhn
	Escribir "Horas extra trabajadas: "
	Leer horaset
	pht<-(horasntnt*valorhn)
	phet<-(horaset*(valorhn*1.25))
	sbase<-phet+pht
	Escribir"Sueldo base: ",sbase
	deducciones<-(sbase*0.14)
	Escribir"Total deducciones: ",deducciones
	Escribir "Numero de hijos del trabajador: "
	leer hijos
	asig<-(250000+(173000*hijos)+180000)
	Escribir"Asignaciones: ",asig
	stotal<-(sbase-deducciones+asig)
	Escribir"Sueldo neto: ",stotal
FinProceso
