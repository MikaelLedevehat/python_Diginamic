import random
import time

t = [5,10,65,61,23,23]

def calcul_moyenne(t):
    moy = 0
    for e in t:
        moy += e

    moy /= len(t)
    return moy

def calcul_occurence(t,e):
    nbOcc = 0
    for i in t:
        if i == e:
            nbOcc += 1

    return nbOcc

def calcul_sup10(t):
    nbElm = 0
    for e in t:
        if e >= 10:
            nbElm += 1

    return nbElm

def calcul_valMax(t):
    nbMax = t[0]
    for e in t:
        if e > nbMax:
            nbMax = e

    return  nbMax

def is_present(t,e):
    for i in t:
        if i == e:
            return True

    return False

print(calcul_moyenne(t))
print(calcul_occurence(t,23))
print(calcul_sup10(t))
print(calcul_valMax(t))
print(is_present(t,23))

def fournis_tab_random(size):
    t2 = []
    for i in range(0,size):
        t2.append(random.randint(0,1000000))

    return t2

def fournis_tab_nEntier_Shuffle(n):
    t2 = []
    for i in range(0,n):
        t2.append(i)

    random.shuffle(t2)
    return t2

print(fournis_tab_random(10))
print(fournis_tab_nEntier_Shuffle(10))
print("----------------")
tab = fournis_tab_random(1000000)

ts = time.time()
print(calcul_moyenne(tab))
print(time.time() - ts)
print("----------------")
ts = time.time()
print(is_present(tab,32))
print(time.time() - ts)