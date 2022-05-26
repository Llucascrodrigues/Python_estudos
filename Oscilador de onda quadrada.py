import turtle as tr
a=100
tr.Turtle()
tr.shape('circle')
#tr.penup()
for i in range(0,10):
    a=a-i
    tr.sety(a)
    tr.forward(10)
    tr.sety(-a)
    tr.forward(10)

    tr.speed(10)
