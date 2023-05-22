import math

print('Enter a floating number:')
x = float(input())

if x < 0 :
    print("This number's square root cannot be calculated")

else:
    square = math.sqrt(x)
    print(square)

