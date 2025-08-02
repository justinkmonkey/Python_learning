import turtle
t1 = turtle.Turtle()
t1.shape('turtle')
t1.color('orange')

while True:
    for i in range(4):
        t1.forward(100)
        t1.left(90)
    t1.left(10)
print('end')




turtle.done()