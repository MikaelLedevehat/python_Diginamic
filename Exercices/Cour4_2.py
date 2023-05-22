truc = []
machin = [None]*5

print(truc, machin)

for i in range(0,3):
    print(i)

for i in range(4,7):
    print(i)

for i in range(2,8,2):
    print(i)

chose = []
chose.extend(range(0,5))

if 3 in chose:
    print("3 est dans la liste")
if 6 in chose:
    print("6 est dans la liste")