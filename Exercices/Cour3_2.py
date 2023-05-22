import math


def cube(arg: float) -> float:
    return arg * arg * arg


def volumeSphere(rayon: float) -> float:
    return 4 / 3 * math.pi * rayon * rayon * rayon


if __name__ == "__main__":
    print(cube(3))
    print(volumeSphere(2.5))
