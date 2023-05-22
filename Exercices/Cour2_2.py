print('Enter a first string:')
s1 = str(input())
print('Enter a second string:')
s2 = str(input())

print("the smallest string is : " + (s1 if len(s1) < len(s2) else s2))
