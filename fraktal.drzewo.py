import turtle

def draw_tree(t, dlugosc, kat, rek):
    if rek > 0:
        
        t.forward(dlugosc)
        t.right(kat)
        draw_tree(t, dlugosc * 0.7, kat, rek - 1)
        t.left(2 * kat)
        draw_tree(t, dlugosc * 0.7, kat, rek - 1)
        t.right(kat)
        t.backward(dlugosc)

t = turtle.Turtle()
t.left(90)  
t.up()
t.backward(150)
t.down()
t.speed(0)
t.color("brown")

draw_tree(t, 100, 60, 7)