Proceso Ejercicio_Calculopromedios
	Escribir"MATEMATICAS"
	Escribir "Ingrese la nota del examen: "
	leer matex
	Escribir "Ingresar notas de las tareas: "
	Leer mat1,mat2, mat3
	avmat<-((matex*0.9)+(((mat1+mat2+mat3)/3)*0.1))
	Escribir "Promedio matematicas: ", avmat
	Escribir"FISICA"
	Escribir "Ingrese la nota del examen: "
	leer fisex
	Escribir "Ingresar notas de las tareas: "
	Leer fis1,fis2
	avfis<-((fisex*0.8)+(((fis1+fis2)/2)*0.2))
	Escribir "Promedio fisica: ", avfis
	Escribir"QUIMICA"
	Escribir "Ingrese la nota del examen"
	leer quimex
	Escribir "Ingresar notas de las tareas"
	Leer quim1,quim2,quim3
	avquim<-((quimex*0.85)+(((quim1+quim2+quim3)/3)*0.15))
	Escribir "Promedio quimica: ",avquim
	promedio<-((avmath+avfis+avquim)/3)
	Escribir"PROMEDIO DE LAS TRES MATERIAS: ", promedio
FinProceso
