name = str.capitalize(input("Sisestage nimi "))
print("Tere " + name)

location = str.capitalize(input("Sisestage oma elukoht: "))
print("Elukoht " + location + " väga lahe , et elad elad mejega ")
    
age = int(input("Vanus:"))
if age <=17:
    print("Kasutaja on liiga noor, et autot juhtida ")
elif age == 18:
    print("olete täiskasvanu ")
else:
    print("Võite autot juhtida ")