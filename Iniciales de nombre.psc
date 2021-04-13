Algoritmo Inicio_Inicialesnombre
	Escribir "Iniciales de nombre:"
	Escribir "Ingresar primer nombre: "
	Leer nombre
	Escribir "Ingresar primer apellido: "
	Leer apellido1
	Escribir "Ingresar segundo apellido: "
	Leer apellido2
	a<-Subcadena(nombre,0,0)
	b<-Subcadena(apellido1,0,0)
	c<-Subcadena(apellido2,0,0)
	Escribir "Iniciales del nombre escrito: " Mayusculas(a),Mayusculas(b),Mayusculas(c)
FinAlgoritmo
