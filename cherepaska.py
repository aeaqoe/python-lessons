# import turtle

# screen = turtle.getscreen()
# t = turtle.Turtle('turtle')
# t.color('orange')
# t.speed(100)

# for i in range(100):
#     t.backward(90)
#     t.left(90)
#     t.pencolor('red')
#     t.left(70)
#     t.backward(83)
#     t.left(83)
#     t.backward(90)
#     t.left(90)
#     t.pencolor('red')
#     t.left(70)
#     t.backward(83)
#     t.left(83)
    
#     t.right(45)
   
# screen.mainloop()
import turtle

screen = turtle.getscreen()
t = turtle.Turtle('turtle')
t.speed(100)



class DrawShape():
    def draw(self, color='red'):
        if self.fill:
            t.color(color)
            t.begin_fill()
        for _ in range(self.side):
            t.forward(self.size)
            t.left(self.angle)
        if self.fill:
            t.end_fill()


class Rect(DrawShape):
    def __init__(self, size, fill=False):
        self.size = size
        self.side = 4
        self.angle = 90
        self.fill = fill
        t.left(90)
        t.backward(120)
        t.right(90)
class Triangle(DrawShape):
    def __init__(self, size, fill=False):
        self.size = size
        self.side = 3
        self.angle = 120
        self.fill = fill
        t.left(90)
        t.forward(360)
        t.right(90)
rect1 = Rect(120, fill=True)
rect1.draw()
rect2 = Rect(120, fill=True)
rect1.draw('yellow')
rect3 = Rect(120, fill=True)
rect1.draw('green')
triangle = Triangle(120, fill=True)
triangle.draw('black')
screen.mainloop()