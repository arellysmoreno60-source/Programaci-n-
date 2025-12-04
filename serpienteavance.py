import turtle
import time

#ventana
ventana=turtle.Screen ()
ventana.title ("Juego de la Serpiente")
ventana.bgcolor ("white")
ventana.setup (width=600, height=600)
ventana.tracer (0)

#serpiente
ser=turtle.Turtle()
ser.direccion="stop"

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


while True:
    ventana.update()
    dibujo (ser,"classic","red",2.5,2.5)
    mover()

    ventana.listen()
    ventana.onkeypress(ar,"Up")
    ventana.onkeypress(iz,"Left")
    ventana.onkeypress(de,"Right")
    ventana.onkeypress(ab,"Down")

    time.sleep (0.1) 


    