def someDiv(nb: int) -> int:
    if nb < 1:
        print("le nombre est icorrect!")
        return 0
    some = 0

    for i in range(1, nb, 1):
        if nb % i == 0:
            some += i

    return some


def estParfait(nb: int) -> bool:
    s = someDiv(nb)
    if s == nb:
        return True
    else:
        return False


def estPremier(nb: int) -> bool:
    s = someDiv(nb)
    if s == 1:
        return True
    else:
        return False


def estChanceux(nb: int) -> bool:
    if nb < 1:
        print("Nombre incorrect")
        return False

    for i in range(0, nb - 1):
        if not estPremier(nb + i + i * i):
            return False

    return True


def autoTest() -> bool:
    if someDiv(12) != 16:
        return False
    if not estParfait(6):
        return False
    if not estPremier(6):
        return False
    if not estChanceux(11):
        return False
