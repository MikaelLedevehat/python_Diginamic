l1 = []
l2 = ["jean", 2, "lisa"]
print(len(l2))
l2[0] = "Marcel"
l2.pop(-1)
l2.insert(0,36)
print(l2)

for i in l2:
    print(i)

for i in range(0,len(l2)):
    print(l2[i])
