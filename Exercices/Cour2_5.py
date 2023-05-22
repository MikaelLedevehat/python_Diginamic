saisie = input("Veuillez saisir un nombre :")

while not saisie.isdigit():
    saisie = input("Veuillez saisir un !!!nombre!!! :")

saisie = int(saisie)
print("Votre nombre est : ", saisie)
