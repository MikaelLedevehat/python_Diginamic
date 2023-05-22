import random

def fournis_tab_random(size):
    t2 = []
    for i in range(0,size):
        t2.append(random.randint(0,1000))

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


t = fournis_tab_random(10)
print(t)
#i = index_minimum(t, 55,60)
#print(i)
tri_bulle(t)
print(t)
