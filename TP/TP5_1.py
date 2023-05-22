import random
import time


def copie(t):
    tbis = []
    for e in t:
        tbis.append(e)
    return tbis

def inverse(t):
    tbis = []
    for e in t:
        tbis.insert(0,e)
    return tbis

def tableau_premier_entier(n):
    t = []
    for i in range(1,n):
        t.append(i)
    return t

def tableau_premier_entier_melange(n):
    t = tableau_premier_entier(n)
    random.shuffle(t)
    return t

def tableau_premier_entier_inverse(n):
    t = tableau_premier_entier(n)
    return inverse(t)

def ligne_dans_fichier(f,n,t):
    f = open(f, "a+")
    f.write(str(n)+"\t"+str(t)+"\n")
    f.close()

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


def temps_tri_bulles(t):
    tab = copie(t)
    ts = time.time()
    tri_bulle(tab)
    tf = time.time() - ts
    return tf

def temps_fct_tri(t, fct):
    tab = copie(t)
    ts = time.time()
    fct(tab)
    tf = time.time() - ts
    return tf

def stats_melange(nmin, nmax, pas, fois, fct):
    for i in range(nmin,nmax,pas):
        moy = 0
        for j in range(0,fois):
            moy += temps_fct_tri(tableau_premier_entier_melange(i), fct)
        moy = moy/fois
        ligne_dans_fichier(fct.__name__+"_melange.txt", i, moy)


def stats_ordone(nmin, nmax, pas, fois, fct):
    for i in range(nmin,nmax,pas):
        moy = 0
        for j in range(0,fois):
            moy += temps_fct_tri(tableau_premier_entier(i),fct)
        moy = moy/fois
        ligne_dans_fichier(fct.__name__+"_ordone.txt", i, moy)

def stats_inverse(nmin, nmax, pas, fois,fct):
    for i in range(nmin,nmax,pas):
        moy = 0
        for j in range(0,fois):
            moy += temps_fct_tri(tableau_premier_entier_inverse(i),fct)
        moy = moy/fois
        ligne_dans_fichier(fct.__name__+"_inverse.txt", i, moy)


stats_melange(100,1000,100,5,tri_extraction)
stats_inverse(100,1000,100,5,tri_insertion)


