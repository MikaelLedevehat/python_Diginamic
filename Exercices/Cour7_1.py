class MaClasse:
    x = 23
    y = x + 5

    def __init__(self,x):
        self.z = 42
        MaClasse.x = x
    def affichage(self):
        print(self.z, self.x, self.y)


if __name__ == "__main__":
    obj = MaClasse(1)
    obj2 = MaClasse(2)
    obj.affichage()
    obj2.affichage()