from os import set_blocking
import turtle
import time 
import random 

delay =0.1
score=0
highestscore=0
#snake body
bodies=[]
#main screen
main_Screen=turtle.Screen()
main_Screen.title('Snake Game')
main_Screen.bgcolour('green')
main_Screen.setup(width=600,height=600)

#Snake Head
head=turtle.Turtle()
head.speed(0)
head.shape('triangular')
head.color('white')
head.fillcolor('blue')
head.penup()
head.goto(0,0)
head.direction='stop'


#Snake Food
food=turtle.Turtle()
food.speed(0)
food.shape('square')
food.color('yellow')
food.fillcolor('red')
food.penup()
food.ht()#hide

food.goto(0.200)
food.st()#show turtle

#score Board
sb=turtle.Turtle()
sb.shape('square')
sb.color('black')
sb.fillcolor('red')
sb.penup()
sb.ht()#hide
food.goto(-280,250)
sb.write('Score: 0 | Highestscore: 0' ,font=('arial',15,'bold'))#font

#function declaration
def moveup():
    if head.direction!='down':
        head.direction='up'

def movedown():
    if head.direction!='up':
        head.direction='down'

def moveleft():
    if head.direction!='right':
        head.direction='left'


def moveright():
    if head.direction!='left':
        head.direction='right'
             

def movestop():
    head.direction='stop'


def move():
    if head.direction!='up':
        y=head.ycor()
        head.sety(y+20)

    if head.direction!='down':
        y=head.ycor()
        head.sety(y-20)

    if head.direction!='left':
        x=head.ycor()
        head.setx(x-20) 

    if head.direction!='right':
        x=head.ycor()
        head.setx(x+20)  

#Event handling
main_Screen.listen()
main_Screen.onkey(moveup,'Up')
main_Screen.onkey(movedown,'Down')
main_Screen.onkey(moveleft,'Left')
main_Screen.onkey(moveright,'Right')
main_Screen.onkey(movestop,'space')

#mainloop
while True:
    main_Screen.update()

    if head.xcor()>280:
        head.setx(-280)#no boundaries ,collosion with boundaries
    if head.xcor()<280:
        head.setx(280)#no boundaries
    if head.ycor()>280:
        head.sety(-280)#no boundaries
    if head.ycor()<280:
        head.sety(280)#no boundaries

    #check collosion with food
    if head.distance(food)<20:#randowm food
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)
        #increase the length of snake
        body=turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape('square')
        x=random.randint(-290,290)
        body.color('red')
        body.fillcolor('darkred')
        bodies.append(body)#append main body bodies
        #increase score with appending main body
        score+=5  #by 5

        #change delay ,speed
        delay -=0.01

        #update the highest score
        if score>highestscore:
            highestscore=score


        sb.clear()
        sb.write('score: {}  | Highest Score: {}'.format(score,highestscore), font=('arial',15,'bold')) 
        #move the snake bodies
    for i in range(len(bodies)-1,0,-1):
        x=bodies[i-1].xcor()#cor=cordinates
        y=bodies[i-1].ycor()
        bodies[i].goto(x,y)
    if len(bodies)>0:
        x=head.xcor()
        y=head.ycor()
        bodies[0].goto(x,y)
    move()  #move function calling 

        #if colllosion  with self body
    for body in bodies:
        if body.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction='stop'

                #hide bodies
            for body in bodies:
                body.ht()
            bodies.clear()
            score=0
            delay=0.1
            #update score board  
            sb.clear()
            
            sb.write('Score: {}  | Highest Score: {}'.format(score,highestscore), font=('arial',15,'bold'))

    time.sleep(delay)
main_Screen.mainloop()
