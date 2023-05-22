def somme(t:(float))-> float:
    somme = 0
    for e in t:
        print(e)
        somme += e
    return somme

print(somme((1,2,3,4,6,7,8,9)))