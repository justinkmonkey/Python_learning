import turtle
import random
t1 = turtle.Turtle()
t1.shape('turtle')
t1.color('blue')
t1.penup()
t2 = turtle.Turtle()
t2.shape('turtle')
t2.color('orange')
t2.penup()




t1.goto(-300,-100)
t2.goto(-300,100)

for i in range(20):
    t1.forward(random.randint(1,50))
    t2.forward(random.randint(1,50))

turtle.done()

