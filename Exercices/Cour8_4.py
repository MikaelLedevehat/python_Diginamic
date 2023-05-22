class CasNormal:
    def uneMethode(self):
        print("CasNormal")

class CasSpecial:
    def uneMethode(self):
        print("CasSpecial")

def fabrique(estNormal:bool=True):
    if estNormal:
        return CasNormal()
    else:
        return CasSpecial()

if __name__ == '__main__':
    c = fabrique(False)
    print(c.uneMethode())

