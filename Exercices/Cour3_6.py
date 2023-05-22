def somme(a: float, b: float, c: float) -> float:
    return a + b + c


if __name__ == "__main__":
    print(somme(*(1, 123, 54)))
