Proceso Ejercicio_Convertidormoneda
	Escribir "Ingrese el valor en chelines austriacos"
	Leer CHA
	PST<-((CHA*956871)/100)
	Escribir CHA, " Chelines equivalen a ", PST, " Pesetas"
	Escribir "Ingrese el valor en Dracmas Griegos"
	Leer DRG
	PST<-((DRG*88607)/100)
	FRA<-(PST/20110)
	Escribir DRA, " Dracmas griegos equivalen a ", FRA," Francos franceses"
	Escribir "Ingresar el valor en pesetas"
	Leer PST
	USD<-(PST/122499)
	LIT<-((PST*100)/9289)
	Escribir PST," Pesetas equivalen a ", USD," Dolares"
	Escribir LIT," Pesetas equivalen a ", LIT," Liras Italianas"
FinProceso
