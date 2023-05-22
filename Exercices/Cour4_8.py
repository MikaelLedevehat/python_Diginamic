def compterMots(s:str):
    list = s.split()
    dictionary = {}
    for e in list:
        if e in dictionary:
            dictionary[e] += 1
        else:
            dictionary[e] = 1
    return dictionary



if __name__ == "__main__":
    print(compterMots("je je suis"))