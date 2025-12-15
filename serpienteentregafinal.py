import turtle
import time
import random

delay= 0.1
score= 0
high_score= 0

#ventana
ventana=turtle.Screen ()
ventana.title ("Juego de la Serpiente")
ventana.bgcolor ("white")
ventana.setup (width=600, height=600)
ventana.tracer (0)

#serpiente
ser=turtle.Turtle()
ser.direccion="stop"

#comida
comida=turtle.Turtle()

#titulo
titulo=turtle.Turtle()
titulo.penup()
titulo.hideturtle()

texto=turtle.Turtle()
texto.penup()
texto.hideturtle()


cola=[]
#si se come una tortuga cola[cuerpo,cuerpo,...]

def dibujo(cuerpo,forma,color,w,h):
    cuerpo.speed(0)
    cuerpo.shape(forma)
    cuerpo.color(color)
    cuerpo.shapesize(w,h)
    cuerpo.penup()

def mover():
    if ser.direccion=="up":
        y=ser.ycor() #10
        ser.sety(y+15) #10+15

    if ser.direccion=="left":
        x=ser.xcor() 
        ser.setx(x-15) 

    if ser.direccion=="right":
        x=ser.xcor() 
        ser.setx(x+15) 

    if ser.direccion=="down":
        y=ser.ycor() 
        ser.sety(y-15) 

def ar():
    ser.direccion="up"
    ser.setheading(90)

def iz():
    ser.direccion="left"
    ser.setheading(180)

def de():
    ser.direccion="right"
    ser.setheading(0)

def ab():
    ser.direccion="down"
    ser.setheading(270)

def comidarandom (comida):
    comida.penup()
    x=random.randint(-260-20,260+20)
    y=random.randint(-260-20,260+20)
    comida.goto(x,y)

def comer (ser,comida):
    if ser.distance(comida) < 20:
        comidarandom(comida)
        cuerpo=turtle.Turtle ()
        dibujo(cuerpo,"square","green",0.5,0.5)
        cola.append (cuerpo)
        return 10

def movercuerpo(ser):
    total=len(cola)
    for i in range (total-1, 0, -1):
        x=cola[i-1].xcor()
        y=cola[i-1].ycor()
        cola[i].goto(x,y)

    if total > 0:
        x=ser.xcor ()
        y=ser.ycor ()
        cola[0].goto (x,y)

def colicionbordes (ser,comida):
    if (ser.xcor() > 290 or ser.xcor () < -290 or ser.ycor() > 290 or ser.ycor() < -290) :
        time.sleep (1)
        ser.reset()
        ser.direccion= "stop"
        for i in cola:
            i.hideturtle ()
        cola.clear ()
        comidarandom (comida)
        return 0

def colicioncuerpo (ser,comida):
    for j in cola:
        if j.distance(ser) < 10:
            time.sleep(1)
            ser.reset()
            ser.direccion="stop"
            for i in cola:
                i.hideturtle()
            cola.clear()
            comidarandom(comida)
            return 0

def marcador(texto,score,hight_score):
    texto.clear()
    texto.write("Score: {}   Hight Score: {}".format(score,hight_score),align="center",font=("arial", 12,"normal"))

titulo.goto(0,220)
titulo.write("Juego de la Serpiente", align="center", font=("arial", 32,"normal"))

titulo.goto(0,160)
titulo.write("Come las tortugas para crecer", align="center", font=("arial", 16,"normal"))

ventana.update()
time.sleep(3)

titulo.clear()
texto.goto(0,260)

comidarandom (comida)
while True:

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


    