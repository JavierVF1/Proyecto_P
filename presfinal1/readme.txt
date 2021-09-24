Panzerquack 1.0v

IDE:Python 3.9.6

1) Iniciar el programa:
	En nuestro IDE de spyder python 3.9.6 abrimos un archivo y vamos a la carpeta que contiene
	el panzerquack v1.0.py, este es el archivo del juego que vamos a ejecutar para que
	comienze el juego.

	Debemos instalar pygame, para esto en la consola debemos escribir
	"pip install pygame", lo cual nos instalará pygame.(OJO ESTO SOLO FUNCIONA EN SPYDER)
	
2)Dentro del juego:
	Debemos presionar espacio para poder comenzar a jugar

	Los 2 tanques aparecen de manera aleatoria a cada lado del mapa

	El jugador de la izquierda (jugador UNO) tiene el primer turno
	para disparar, para realizar esto debemos ingresar en consola los datos
	de velocidad y posteriormente el angulo, posteriormente se disparará el
	proyectil, dejando una estela tras el para poder identificar su movimiento, una vez
	colisiona con el suelo o con los bordes del mapa es turno del segundo jugador
	que tendrá que realizar la misma acción
	
	-Sobre los datos:
		EL VALOR DE VELOCIDAD:
			La velocidad se recomienda no pasarse de 8, desde este valor en adelante el
			proyectil va a chocar si o si con los bordes del mapa, pues va con demasiada
			velocidad como para realizar una parabola en el mapa.
		EL VALOR DE ANGULO:
			El angulo para los tanques depende hacia adonde esté el enemigo, por ello el tanque de la izquierda
			y el de la derecha se apuntan, es decir, el tanque de la derecha tiene invertido el angulo para que dispare
			hacia el tanque de la izquierda con angulos desde 0 a 90 (esto es solo una recomendación, es posible disparar hacia atrás
			con el tanque si es necesario)
3)ERRORES Y BUGS:
	a)Algunas veces al comenzar el juego el tanque UNO al disparar no realiza la animación, a pesar de esto el proyectil realiza la trayectorioa, aunque no es visible
	b)A veces el programa tiene un error y es que solo funciona uno de los dos tanques en vez de los 2, para solucionar esto debemos cerrar y abrir nuevamente la ejecución