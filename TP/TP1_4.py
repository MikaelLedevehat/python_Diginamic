import random

print(random.randint(10,20))
print(random.randrange(5))
print(random.randrange(5,10))
print(random.choice(("jean", "marcel", "brutus")))
l = ["jean", "marcel", "brutus"]
random.shuffle(l)
print(l)
