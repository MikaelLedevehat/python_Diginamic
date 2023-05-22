import random
import math

def fournis_tab_random(size):
    t2 = []
    for i in range(0,size):
        t2.append(random.randint(0,size))

    return t2


def index_minimum(t,d,f):
    if len(t) < f:
        return
    val = d
    for i in range(d,f):
        if t[i] < t[val]:
            val= i

    return val

def index_minimum(t,d,f):
    if len(t) < f:
        return
    val = t[d]
    for i in range(d,f):
        if t[i] < val:
            val = t[i]

    return val


def insertion(t, v, d, f):
    a = d
    b = f
    while a <= b:
        m = (a+b)//2
        if t[m] == v:
            t.insert(m,v)
            return
        elif t[m] < v:
            a = m + 1
        else:
            b = m - 1
    if v < t[m]:
        t.insert(m,v)
    else:
        t.insert(m+1, v)
    return


def tri_extraction(t):
    for i in range(0,len(t)-1):
        min = index_minimum(t,i,len(t))
        save = t[min]
        t[min] = t[i]
        t[i] = save


def tri_insertion(t):
    for i in range(1,len(t)):
        insertion(t, t[i], 0, i-1)
        val = t.pop(i+1)



t = fournis_tab_random(10)
print(t)
#tri_extraction(t)
tri_insertion(t)
print(t)
