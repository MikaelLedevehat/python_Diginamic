from math import sin

for x in range(-3, 3):
    try:
        r = sin(x) / x
    except ZeroDivisionError:
        print("infinite, division by 0")
    else:
        print(r)
