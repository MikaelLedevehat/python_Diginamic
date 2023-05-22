import math


def trinomeCalcul(a:float, b:float, c:float) -> tuple:
    delta = b*b - 4 * a * c
    nbRacine = 0
    listRacine = []
    if delta > 0:
        nbRacine = 2
        listRacine.append((-b-math.sqrt(delta))/(2*a))
        listRacine.append((-b+math.sqrt(delta))/(2*a))

    elif delta == 0:
        nbRacine = 1
        listRacine.append(-b/2*a)

    else:
        nbRacine = 0

    return (nbRacine, *listRacine)
