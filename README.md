Juego de la Serpiente
UNIVERSIDAD INTERNACIONAL DEL ECUADOR
Latacunga, jueves 17 de diciembre de 2025.
-

INTRODUCCIÓN
-
Es un juego muy popular en el que el usuario controla una serpiente continuamente por la pantalla. Su objetivo principal es comer la comida (tortuga) que aparece en distintas partes de la pantalla para crecer su tamaño y aumentar la puntuación. 
A medida que va creciendo el juego se dificulta ya que el usuario debe evitar: chocar con los bordes de la pantalla y contra su propio cuerpo. 

•	OBJETIVO
-
Crear un juego divertido para los niños, jóvenes y adultos desarrollando sus habilidades cognitivas mientras se distraen y disfrutan en un espacio totalmente seguro y cómodo a través de la pantalla. 
•	CONCEPTOS CLAVE
Turtle 
Es un módulo gráfico de Python que permite dibujar y mover objetos en una ventana. Funcionando como una tortuga según las instrucciones que le demos. 

Random
El módulo random sirve para generar valores aleatorios como la comida
Ejemplo:
random.randint(-260-20,260+20)

Time
Este módulo controla la velocidad de la serpiente y crea pausas entre cada movimiento. 
La función más común es:
time.sleep(0.1)

Funciones
Permiten organizar el código y reutilizarlo.
Se utiliza para: Mover la serpiente, cambiar la dirección, reiniciar el juego.
Ejemplo:
•	def mover():
     if ser.direccion=="up":
     
Return
Se usa dentro de una función para devolver un valor.
En el juego sirve para: Devolver el estado del juego, comprobar colisiones o condiciones.
Ejemplo:
def colicionbordes (ser,comida):
    if (ser.xcor() > 290 or ser.xcor () < -290 or ser.ycor() > 290 or ser.ycor() < -290) :
    return 0
    
Ventana.update() 
Se actualiza manualmente la pantalla.
Se usa junto con ventana.tracer(0). Evitar parpadeos y controla cuándo se redibuja el juego.

Delay
Controla la velocidad y es ideal para aumentar la dificultad del juego.
Se logra usando:
time.sleep(delay)
Un delay pequeño → juego más rápido
Un delay grande → juego más lento

•	VARIABLES 
-
delay/score/high_score
ventana
ser
comida
titulo
texto
ser.direccion
cola

•	FUNCIONES
-
def dibujo(cuerpo,forma,color,w,h)
def mover():
def ar():/def iz():/def de():/def ab():
def comidarandom (comida):
def comer (ser,comida):
def movercuerpo(ser):
def colicionbordes (ser,comida):
def colicioncuerpo (ser,comida):
def marcador(texto,score,hight_score):

•	WHILE TRUE
-
    ventana.update()
    dibujo (ser,"classic","red",2.5,2.5)
    dibujo (comida,"turtle","green",1,1)
    if colicionbordes(ser,comida) == 0 or colicioncuerpo(ser,comida) == 0:
        if score > high_score:
            high_score = score
        score=0
    
    if comer (ser,comida) == 10:
        score+=10
   
    movercuerpo(ser)
    marcador(texto,score,high_score)
    mover()
    
    ventana.listen()
    ventana.onkeypress(ar,"Up")
    ventana.onkeypress(iz,"Left")
    ventana.onkeypress(de,"Right")
    ventana.onkeypress(ab,"Down")
    time.sleep (delay)
Todos estos comandos son los que se repiten en el bucle ya que la serpiente vuelve a moverse, comer y chocar contra si misma o los bordes. El marcador se suma de 10, el movimiento de la serpiente está dirijido por el usuario por las teclas asignadas. 

•	CONCLUSION
-
Las clases previamente vistas han sido de gran ayuda y entendimiento al momento del desarrollo del juego, sin embargo, para que sea más eficaz es necesaria la búsqueda externa. La programación abre la puerta de la imaginación, entre otras habilidades cognitivas para nuestro desarrollo. 
