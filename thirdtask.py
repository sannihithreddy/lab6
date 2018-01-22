import turtle
def draw_rectangle( width, height):
        t = turtle.Turtle()
        t.up()
        t.down()
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)


#width = float(print(input("Enter width")))
#height =float( print(input("Enter height")))
draw_rectangle(100,300)
turtle.mainloop()
