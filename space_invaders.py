
#Set up the screen
#python 3.5

import turtle
import os
import math
import random

#Set up the screen
wn=turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")





#Draw border

border_pen=turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-275,-225)
border_pen.pendown()
border_pen.pensize(3)
for side in range(2):
    
    border_pen.fd(550)
    border_pen.lt(90)
    border_pen.fd(450)
    border_pen.lt(90)
border_pen.hideturtle()

#Set the score
score=0

#Draw the score
score_pen=turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-265,230)
scorestring="Score: %s" %score
score_pen.write(scorestring, False, align="left",font=("Arial",14,"normal"))
score_pen.hideturtle()


#Create the player turtle

player=turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-215)
player.setheading(90)


playerspeed=15



#Create a no of enemies
number_of_enemies=5
#Create an empty list
enemies=[]

#Add enemies to the list
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

#Create the enemy

for enemy in enemies:
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x=random.randint(-200,200)
    y=random.randint(100,210)
    enemy.setposition(x,y)

enemyspeed=2

#Create the player's bullet
bullet=turtle.Turtle()
bullet.color("yellow")
bullet.shape('triangle')
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed=20

#Define bullet state
#ready-ready to fire
#fire-bullet is firing
bulletstate="ready"


#Move the player left and right
def move_left():
    x=player.xcor()
    x-=playerspeed
    if x<-260:
        x=-260
    player.setx(x)

def move_right():
    x=player.xcor()
    x+=playerspeed
    if x>260:
        x=260
    player.setx(x)

def fire_bullet():
    #declare bulletstate as global if it needs changing
    global bulletstate
    if bulletstate=="ready":
        bulletstate="fire"
        #Move the bullet to just above the player

        x=player.xcor()
        y=player.ycor()+10
        bullet.setposition(x,y)
        bullet.showturtle()

def isCollision(t1,t2):
    distance=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance<15:
        return True
    else:
        return False
    

#Create keyboard function

turtle.listen()
turtle.onkey(move_left,"Left")
turtle.onkey(move_right,"Right")
turtle.onkey(fire_bullet,"space")

#Main game loop

while True:
    for enemy in enemies:
        #Move the enemy
        x=enemy.xcor()
        x+=enemyspeed
        enemy.setx(x)

        #Move the enemy back and down

        if enemy.xcor()>260:
            for e in enemies:
                y=e.ycor()
                y-=30
                e.sety(y)
            enemyspeed*=-1   

        if enemy.xcor()<-260:
            for e in enemies:
                y=e.ycor()
                y-=30
                e.sety(y)
            enemyspeed*=-1

        #Check for collision between bullet and the enemy

        if isCollision(bullet,enemy):
            #Reset the  bullet
            bullet.hideturtle()
            bulletstate="ready"
            bullet.setposition(0,-400)
            #Reset the enemy
            x=random.randint(-200,200)
            y=random.randint(100,210)
            enemy.setposition(x,y)
            #Update the score
            score+=10
            scorestring="Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left",font=("Arial",14,"normal"))
            
            


        if isCollision(enemy,player):
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break
        

    #Move the bullet
    if bulletstate=="fire":    
        y=bullet.ycor()
        y+=bulletspeed
        bullet.sety(y)

    #check border for bullet

    if bullet.ycor()>215:
        bullet.hideturtle()
        bulletstate="ready"


    

delay=input("Press Enter to Finish")
