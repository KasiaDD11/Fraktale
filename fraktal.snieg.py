import turtle

def krzywa_kocha(zolw, dlugosc, stopien):
    if stopien == 0:
        zolw.forward(dlugosc)
    else:
        nowa_dlugosc = dlugosc / 3
        krzywa_kocha(zolw, nowa_dlugosc, stopien - 1)
        zolw.left(60)
        krzywa_kocha(zolw, nowa_dlugosc, stopien - 1)
        zolw.right(120)
        krzywa_kocha(zolw, nowa_dlugosc, stopien - 1)
        zolw.left(60)
        krzywa_kocha(zolw, nowa_dlugosc, stopien - 1)

def rysuj_platek(dlugosc, stopien):
    okno = turtle.Screen()
    zolw = turtle.Turtle()
    zolw.speed(0) 
    for _ in range(3):
        krzywa_kocha(zolw, dlugosc, stopien)
        zolw.right(120)

    okno.exitonclick()


rysuj_platek(150, 3)