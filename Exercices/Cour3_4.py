import math


def voldMassElipsoide(a: float = 1, b: float = 1,
                      c: float = 1, mv: float = 1) -> (float, float):
    volume = 4 / 3 * math.pi * a * b * c
    masse = mv * volume

    return (masse, volume)


print(voldMassElipsoide(10.54, 9.2))
