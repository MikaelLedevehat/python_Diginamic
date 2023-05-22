class Vecteur2D:

    def __new__(cls, *args, **kwargs):

        print("1. Create a new instance of Vecteur2D.")

        return super().__new__(cls)


    def __init__(self, x=0, y=0):

        print("2. Initialize the new instance of Vecteur2D.")

        self.x = x

        self.y = y

    def __repr__(self) -> str:
        return f"{type(self).__name__}(x={self.x}, y={self.y})"

    def __add__(self, other):
        return Vecteur2D(self.x + other.x, self.y + other.y)


if __name__ == "__main__":
    v1 = Vecteur2D(1)
    v2 = Vecteur2D(2,3)
    print(v1+v2)
