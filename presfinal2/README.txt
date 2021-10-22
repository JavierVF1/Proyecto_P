Panzerquack POO

IDE:Python 3.9.6

1) Iniciar el programa:
	En nuestro IDE de spyder python 3.9.6 abrimos un archivo y vamos a la carpeta que contiene
	el panzerquack POO.py, este es el archivo del juego que vamos a ejecutar para que
	comienze el juego.

	Debemos instalar pygame, para esto en la consola debemos escribir
	"pip install pygame", lo cual nos instalará pygame.(OJO ESTO SOLO FUNCIONA EN SPYDER)
	
2)Dentro del juego:
	Debemos presionar espacio para poder comenzar a jugar

	Los 2 tanques aparecen de manera aleatoria a cada lado del mapa

	El turno se marca en la parte inferior derecha del juego, además aparece la vida del jugador
	que está de turno
	
	-Sobre ingresar los datos:
		EL TIPO DE BALA
			El tipo de proyectíl es lo primero que se nos pregrunta, este proyectil se
			selecciona según un cuadro de texto que aparece en pantalla en forma de listado
			, en el recuadro marcado de gris hacemos click y seleccionamos el proyectíl según su numero
			en la lista.
		EL VALOR DE VELOCIDAD:
			La velocidad está implementada de manera que se ingrese en un recuadro, en la ventana parte superior
			derecha, una vez ingresado el valor de velocidad presionar enter.
		EL VALOR DE ANGULO:
			El angulo para los tanques depende hacia adonde esté el enemigo, por ello el tanque de la izquierda
			y el de la derecha se apuntan, es decir, el tanque de la derecha tiene invertido el angulo para que dispare
			hacia el tanque de la izquierda con angulos desde 0 a 90 (esto es solo una recomendación, es posible disparar hacia atrás
			con el tanque si es necesario), para ingresar el angulo es igual que con la velocidad, hacemos click en el recuadro que está
			arriba a la derecha y clickamos enter
		TRAS LOS PASOS ANTERIORES:
			Tras estos pasos el jugador que está de turno dispara el proyectil, una vez ah disparado este la bala realiza la trayectoria definida según
			los parametros que se dieron, luego procede al turno del siguiente jugador que, si su vida es mayor a 0, podrá disparar, si no este jugador 
			ha perdido la partida.