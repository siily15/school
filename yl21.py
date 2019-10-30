import random

yMin=0
yMax=100
algarv=101
goal=random.randint(yMin,yMax)

while algarv != goal:
    algarv = int(input("Arv "))
    if algarv < goal:
        print("Arv on liiga väike" )
    elif algarv > goal:
        print("Arv on liiga suur ")
print("Õige vastus") 