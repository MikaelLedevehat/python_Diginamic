def table(base, debut, fin, inc):
    for i in range(debut, fin, inc):
        print(base[i])


if __name__ == '__main__':
    table(["marcel", "proust", 1, 56], 2, 4, 1)
