import turtle as ttl  
import time  
import random as rdm  
# Here we will be creating a window screen  
window_screen = ttl.Screen()  
window_screen.title("Snake Game By Riket")  
window_screen.bgcolor("black")  
   
   
delay = 0.1  
score = 0  
high_score = 0  
  

# The width and height can be put as user's choice  
window_screen.setup(width = 650, height = 650)  
window_screen.tracer(0)  
   
   
# Here, we will create the head of the snake  
head = ttl.Turtle()  
head.shape("circle")  
head.color("white")  
head.penup()  
head.goto(0, 0)  
head.direction = "Stop"  
   
   
# Here, we will create the food in the game  
food1 = ttl.Turtle()  
colors = rdm.choice(['pink', 'yellow', 'blue'])  
shapes = rdm.choice(['triangle', 'square', 'circle'])  
food1.speed(0)  
food1.shape(shapes)  
food1.color(colors)  
food1.penup()  
food1.goto(0, 100)  
   
   
pen1 = ttl.Turtle()  
pen1.speed(0)  
pen1.shape("square")  
pen1.color("white")  
pen1.penup()  
pen1.hideturtle()  
pen1.goto(0, 250)  
pen1.write("Score: 0, High Score: 0", align = "center",  
          font = ("arial", 22, "bold"))  
# Here, we will assign the key directions  
def group1():  
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
        y1 = head.ycor()  
        head.sety(y1 + 20)  
    if head.direction == "down":  
        y1 = head.ycor()  
        head.sety(y1 - 20)  
    if head.direction == "left":  
        x1 = head.xcor()  
        head.setx(x1 - 20)  
    if head.direction == "right":  
        x1 = head.xcor()  
        head.setx(x1 + 20)  
   
   
window_screen.listen()  
window_screen.onkeypress(group1, "Up")  
window_screen.onkeypress(go_down, "Down")  
window_screen.onkeypress(go_left, "Left")  
window_screen.onkeypress(go_right, "Right")  
  
segments1 = []  
   
# Code for main gameplay  
while True:  
    window_screen.update()  
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:  
        time.sleep(1)  
        head.goto(0, 0)  
        head.direction = "Stop"  
        colors = rdm.choice(['pink', 'blue', 'yellow'])  
        shapes = rdm.choice(['square', 'circle'])  
        for segment1 in segments1:  
            segment1.goto(1050, 1050)  
        segments1.clear()  
        score = 0  
        delay = 0.1  
        pen1.clear()  
        pen1.write("Score: {} Highest Score: {} ".format(  
            score, high_score), align = "center", font = ("arial", 24, "bold"))  
    if head.distance(food1) < 20:  
        x1 = rdm.randint(-275, 275)  
        y1 = rdm.randint(-275, 275)  
        food1.goto(x1, y1)  
   
        # Here, we are adding segment  
        segment = ttl.Turtle()  
        segment.speed(0)  
        segment.shape("square")  
        segment.color("orange")  # tail colour  
        segment.penup()  
        segments1.append(segment)  
        delay -= 0.001  
        score += 10  
        if score > high_score:  
            high_score = score  
        pen1.clear()  
        pen1.write("Score : {} Highest Score : {} ".format(  
            score, high_score), align = "center", font = ("arial", 22, "bold"))  
    # Checking for head collisions with body segments  
    for index in range(len(segments1)-1, 0, -1):  
        x1 = segments1[index - 1].xcor()  
        y1 = segments1[index - 1].ycor()  
        segments1[index].goto(x1, y1)  
    if len(segments1) > 0:  
        x1 = head.xcor()  
        y1 = head.ycor()  
        segments1[0].goto(x1, y1)  
    move()  
    for segment1 in segments1:  
        if segment1.distance(head) < 20:  
            time.sleep(1)  
            head.goto(0, 0)  
            head.direction = "stop"  
            colors = rdm.choice(['pink', 'blue', 'yellow'])  
            shapes = rdm.choice(['square', 'triangle'])  
            for segment1 in segments1:  
                segment1.goto(1050, 1050)  
            segment1.clear()  
   
            score = 0  
            delay = 0.1  
            pen1.clear()  
            pen1.write("Score: {} Highest Score: {} ".format(  
                score, high_score), align = "center", font = ("arial", 22, "bold"))  
    time.sleep(delay)  
   
window_screen.mainloop()  
