class Rectangle:

    def __init__(self, longueur:float=10, largeur:float=10):
        self.longueur = longueur
        self.largeur = largeur
        self.nom = "Rectangle"

    def __repr__(self) -> str:
        return f"{type(self).__name__}(nom={self.nom}, longueur={self.longueur}, largeur={self.largeur})"

    def surface(self) -> float:
        return self.largeur * self.longueur


class Carre(Rectangle):

    def __init__(self, s):
        self.longueur = s
        self.largeur = s
        self.nom = "Carre"

if __name__ == "__main__":
    r = Rectangle(20,30)
    print(r)
    r1 = Carre(40)
    print(r1)