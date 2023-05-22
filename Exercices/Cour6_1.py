from module_calcul_racine import *
from easygui import *

if __name__ == "__main__":
    a = integerbox("Saisissez a:")
    b = integerbox("Saisissez b:")
    c = integerbox("Saisissez c:")

    msgbox(trinomeCalcul(a,b,c), "Voici le nombre de racines, ansi que les racine du trinome")