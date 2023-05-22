from easygui import msgbox

from parfait_chanceux_m import *


if __name__ == "__main__":
    parfaits = []
    chanceux = []

    for i in range(2, 1001):
        if estParfait(i):
            parfaits.append(i)
        if estChanceux(i):
            chanceux.append(i)

    msgbox(parfaits,"Voici les nombres parfaits")
    msgbox(chanceux,"Voici les nombres chanceux")

