pSeuil = 2.3
vSeuil = 7.41

print('Enter current speaker volume:')
volume = float(input())
print('Enter current speaker pressure:')
pressure = float(input())

if volume > vSeuil and pressure > pSeuil:
    print("Stopping immediately")
    exit(0)
elif pressure > pSeuil and volume <= vSeuil:
    print("Up the volume a bit")
elif volume > vSeuil and pressure <= pSeuil:
    print("Down the volume a bit")
else:
    print("Everything is fine!")

