setX = {"a", "b", "c", "d"}
setY = {"s", "b", "d"}

print(setX)
print(setY)

print("c" in setX)
print("a" in setY)

print(setX.difference(setY))
print(setY.difference(setX))
print( setX.union(setY))
print( setX.intersection(setY))