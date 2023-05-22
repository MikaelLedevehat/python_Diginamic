class Point():
    def __init__(self,x:float = 0.0,y:float = 0.0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x},{self.y})"

class Segment():
    def __init__(self,x1,y1,x2,y2):
        self.origin = Point(x1,y1)
        self.extremite = Point(x2,y2)

    def __repr__(self):
        return f"Segment : origine = {self.origin}, extremite = {self.extremite}"

if __name__ == "__main__":
    s = Segment(0,0,19.3,55.2)
    print(s)
    s1 = Segment(1,2,3,4)
    print(s1)


