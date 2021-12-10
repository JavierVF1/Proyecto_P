Panzerquack POO

IDE:Python 3.9.6

1) Iniciar el programa:
	En nuestro IDE de spyder python 3.9.6 abrimos un archivo y vamos a la carpeta que contiene
	el panzerquack POO.py, este es el archivo del juego que vamos a ejecutar para que
	comienze el juego.

	Debemos instalar pygame, para esto en la consola debemos escribir
	"pip install pygame", lo cual nos instalará pygame.(OJO ESTO SOLO FUNCIONA EN SPYDER)
	
2)Dentro del juego:
	Se nos abrirá la pantalla de menú la cual nos dará a escoger tres opciones las cuales son “Comenzar el Juego”, “Configuraciones” y Salir. 

-Al comenzar el juego este cargara con los valores predefinidos por defecto, estos valores son tamaño de la pantalla, numero de jugadores y bots, cantidad de balas y afectos de entorno.
-Los valores mínimos (por defecto) y máximos se encuentran en el menú de configuraciones, estos están ubicados a la derecha de la textbox. Una vez ingresados los valores deseados se vuelve automáticamente al menú principal para luego dar inicio al juego.
-Una vez iniciado el juego los turnos serán randomicos al igual que el spawn y el mapa, los bots tendrán prioridad de tiro. 
-Cada turno se compone mediante tres pasos los cuales son selección de bala, velocidad y Angulo

EL TIPO DE BALA
-El tipo de proyectil es lo primero que se nos pregunta, este proyectil se selecciona según un cuadro de texto que aparece en pantalla en forma de listado, en el recuadro marcado de negro, seleccionamos el proyectil según su número en la lista.

EL VALOR DE VELOCIDAD:
-La velocidad está implementada de manera que se ingrese en un recuadro, en la ventana parte superior derecha, una vez ingresado el valor de velocidad presionar enter.

EL VALOR DE ANGULO:
-Adjuntaremos una imagen llamada “ángulos” el cual nos ayudara a elegir donde queremos apuntar el disparo de la bala

TRAS LOS PASOS ANTERIORES:
-Tras estos pasos el jugador que está de turno dispara el proyectil, una vez ha disparado este la bala realiza la trayectoria definida según los parámetros que se dieron, luego procede al turno del siguiente jugador
-Para lograr ser el ganador en el juego tendrá que matar a la mayor cantidad de tankes posibles, ganará el tanke que allá matado más contrincantes. Si los jugadores se llegan quedar sin balas el juego termina en empate. Si los jugadores matan a la misma cantidad de jugadores el juego terminara en empate.
 luego procede al turno del siguiente jugador.

3)Errores o bugs
-Primero que nada, quedan numeros magicos y falta restructurar el codigo para aumentar la eficiencia.
-Al dejar jugndo el codigo solo medinte bots se queda pegado al transcurso de unos minutos jugndo solo.
-Al colicionar una bala que destruye el terreno a su alrrededor (bala105mm) con el vorde del mapa este genera un error el cual nos dice que la lista se salio del rngo esto es entendible ya que quiere modificar un valor de la lista que no existe. 
world_data[posiciony][posicionx+1] = 0
IndexError: list assignment index out of range
-Es posible seguir encontrndo errores esto ya que a nuestro grupo en lo personal nos falto tiempo para afinar detalles.