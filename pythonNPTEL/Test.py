import turtle as tt

pen = tt.Turtle()

j=0
pen.color('green')
pen.penup()
pen.setpos(30,30)

while(j <6):
    pen.pendown()
    for i in range(10):
        pen.circle(25)
    j += 1

tt.done()
