# Simple Snake Game in Python 3 


import turtle
import time
import random

delay = 0.1

# Score
Pontuacao = 0
Pontuacao_maxima = 0

# Set up da tela
wn = turtle.Screen()
wn.title("Snake Game by Luan Jesus")
wn.bgcolor("purple")
wn.setup(width=600, height=600)
wn.tracer(0) 

# Snakehead
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []


pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Pontuacao:0  Pontuacao maxima:0", align="center", font=("Courier", 22, "normal"))

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main game loop
while True:
    wn.update()

    
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        
        for segment in segments:
            segment.goto(1000, 1000)
        
      
        segments.clear()

       
        Pontuacao = 0

        
        delay = 0.1

        pen.clear()
        pen.write("Pontuacao: {}  Pontuacao maxima: {}".format(Pontuacao, Pontuacao_maxima), align="center", font=("Courier", 22, "normal")) 


    
    if head.distance(food) < 20:
        
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

       
        delay -= 0.001

       
        Pontuacao += 10

        if Pontuacao > Pontuacao_maxima:
            Pontuacao_maxima = Pontuacao
        
        pen.clear()
        pen.write("Pontuacao: {}  Pontuacao maxima: {}".format(Pontuacao, Pontuacao_maxima), align="center", font=("Courier", 22, "normal")) 

    
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

   
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()    

    
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
        
            
            for segment in segments:
                segment.goto(1000, 1000)
        
            
            segments.clear()

           
            Pontuacao = 0

            
            delay = 0.1
        
            
            pen.clear()
            pen.write("Pontuacao: {}  Pontuacao maxima: {}".format(Pontuacao, Pontuacao_maxima), align="center", font=("Couriaer", 22, "normal"))

    time.sleep(delay)

wn.mainloop()
