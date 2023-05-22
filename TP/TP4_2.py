import random

def fournis_tab_random(size):
    t2 = []
    for i in range(0,size):
        t2.append(random.randint(0,size))

    return t2


def index_minimum(t,d,f):
    if len(t) < f:
        return
    val = t[d]
    for i in range(d,f):
        if t[i] < val:
            val = t[i]

    return val

def tri_bulle(t):
    tourBoucleActuel = 0
    currVall = 0
    for j in range(0, len(t) - tourBoucleActuel):
        for i in range(0, len(t) - 1):
            if t[i] > t[i + 1]:
                save = t[i]
                t[i] = t[i + 1]
                t[i + 1] = save
        tourBoucleActuel += 1

def recherche_ordone(t,nb):
    currVall = 0
    while nb != t[currVall]:
        if t[currVall]>nb:
            return -1
        else:
            currVall += 1
    return currVall

def dichotomie(t, v):
    a = 0
    b = len(t) - 1
    while a <= b:
        m = (a + b) // 2
        if t[m] == v:
            return m
        elif t[m] < v:
            a = m + 1
        else:
            b = m - 1
    return -1

def insertion(t, v):
    a = 0
    b = len(t) - 1
    while a <= b:
        m = (a + b) // 2
        if t[m] == v:
            t.insert(m,v)
            return
        elif t[m] < v:
            a = m + 1
        else:
            b = m - 1
    t.insert(m,v)
    return


t = fournis_tab_random(10)
tri_bulle(t)
print(t)
print(recherche_ordone(t,5))
print(dichotomie(t, 5))
print(t)
insertion(t,5)
print(t)
