a = int(input("Sisestage esimene arv "))
b = int(input("Sisestage teine arv "))
c = int(input("Sisestage kolamas arv "))

if  a > b and a > c:
    maximum = a
elif b > c:
    maximum = b
elif b > c:
    maximum = c
     
print("maximu on: " + str(maximum))  