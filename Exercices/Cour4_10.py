def Pile(*args) -> list:
    return [x for x in args]


def Empile(e, pile: list):
    pile.append(e)


def Depile(pile:list):
    return pile.pop()


if __name__ == "__main__":
    lifo = Pile("coucou", 2);
    print(lifo)
    Empile(56, lifo)
    print(lifo)
    e = Depile(lifo)
    print(e)
    print(lifo)

