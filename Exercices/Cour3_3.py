from easygui import *
def maFunction(x: float) -> float:
    return 2 * 3 + x - 5


def tabuler(fonction, borneInf, borneSup, nbPas):
    if borneInf >= borneSup:
        raise Exception("La borne inferieur est invalide")
    for i in range(borneInf, borneSup, nbPas):
        print(fonction(i))


if __name__ == "__main__":
    borneInf = integerbox("Borne inf")
    borneSupp = integerbox("Borne Supp")
    pas = integerbox("pas")
    tabuler(maFunction, borneInf, borneSupp, pas)
