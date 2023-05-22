from easygui import *

listeEntier = [5,79,2,34,1]

saisie = integerbox()

trouve = False
for e in listeEntier:
    if e == saisie:
        msgbox("trouvé")
        trouve = True
        break

if not trouve:
    msgbox("Le nombre que vous avez saisi n'est pas dans la liste")

saisiePositif = integerbox("Saisissez un entier positif")
'''while saisiePositif > 0:
    saisiePositif = integerbox("Saisissez un entier positif")'''

i = 2
flag = False
while i < saisiePositif:
    if saisiePositif % i == 0:
        flag = True
        msgbox("Ce nombre est le premier diviseur trouvé "+ str(i) + ". Le nombre saisi n'est pas premier")
        break
    i += 1

if not flag:
    msgbox("Ce nombre est premier")
