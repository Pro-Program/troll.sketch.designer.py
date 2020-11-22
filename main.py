import turtle
import random
import time
print("Gacha Gord.exe has stopped responding")
chicken = turtle.Turtle()
chickenscreen = turtle.Screen()
chicken.speed(20)
def fnw():
  chicken.forward(10)
def fna():
  chicken.left(10)
def fns():
  chicken.backward(10)
def fnd():
  chicken.right(10)
def p():
  chicken.penup()
def q():
  chicken.pendown()
def beginfill():
  chicken.begin_fill()
def endfill():
  chicken.end_fill()


#def endfill()
  #loop forever
  #changes a random number of seconds
def GachaGord():
  while True:
    time.sleep(0.1)
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    chicken.pencolor((red,green,blue))
    #tuple: (5,4,2,2,1) -> (5,4,2,1
#run function  

#stop drawing    .penup()
#start drawing   .pendown()

#.stamp()
#.begin_fill()  .end_fill()

chickenscreen.setup(800,800)
chickenscreen.onkey(fns,"w")
chickenscreen.onkey(fnd,"a")
chickenscreen.onkey(fnw,"s")
chickenscreen.onkey(fna,"d")
chickenscreen.onkey(p,"e")
chickenscreen.onkey(q,"q")
chickenscreen.onkey(beginfill,"b")
chickenscreen.onkey(endfill,"c")
chickenscreen.listen()
GachaGord()
