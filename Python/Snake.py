#Snake
import turtle
import time
import random

posp = 0.1

#Score
score = 0
high_score = 0


#window configuration
nw = turtle.Screen()
nw.title("PizzaKaan")
nw.bgcolor("black")
nw.setup(width = 600, height = 600)
nw.tracer(0)

#Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("green")
head.penup()
head.goto(0,0)
head.direction = "stop"

#Food (Pizza)
food = turtle.Turtle()
food.speed(0)
food.shape("triangle")
food.color("yellow")
food.penup()
food.goto(0,100)

#Snake body
seg = []

#Score
text = turtle.Turtle()
text.speed(0)
text.color("white")
text.penup()
text.hideturtle
text.goto(0,260)
text.write("Score: 0    High Score: 0", align = "center", font = ("Courier",24, "normal"))

#Functions
def up():
    head.direction = "up"
def down():
    head.direction = "down"
def left():
    head.direction = "left"
def right():
    head.direction = "right"

def mov():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

#Keyboard
nw.listen()
nw.onkeypress(up, "Up")
nw.onkeypress(down, "Down")
nw.onkeypress(left, "Left")
nw.onkeypress(right, "Right")

while True:
    nw.update()

    #Edge collisions
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        #hide segments
        for segment in seg:
            segment.goto(2000,2000)

        #Clean segments list
        seg.clear()

        #Reset Score
        score = 0
        text.clear()
        text.write("Score: {}    High Score: {}".format(score, high_score), align = "center", font = ("Courier",24, "normal"))

    #Food collisions
    if head.distance(food) < 20:
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        food.goto(x,y)

        new_seg = turtle.Turtle()
        new_seg.speed(0)
        new_seg.shape("circle")
        new_seg.color("green")
        new_seg.penup()
        seg.append(new_seg)

        #Increase score
        score += 10

        if score > high_score:
            high_score = score
        
        text.clear()
        text.write("Score: {}    High Score: {}".format(score, high_score), align = "center", font = ("Courier",24, "normal"))

    #Move the snake body
    totalSeg = len(seg)
    for index in range(totalSeg -1, 0, -1):
        x = seg[index - 1].xcor()
        y = seg[index - 1].ycor()
        seg[index].goto(x,y)

    if totalSeg > 0:
        x = head.xcor()
        y = head.ycor()
        seg[0].goto(x,y)


    mov()

    #Body collisions
    for segment in seg:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            #Hide segments
            for segment in seg:
                segment.goto(2000,2000)

            #Clean segment list
            seg.clear()

            #Reset score
            score = 0
            text.clear()
            text.write("Score: {}    High Score: {}".format(score, high_score), align = "center", font = ("Courier",24, "normal"))

    time.sleep(posp)
