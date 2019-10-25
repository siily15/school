text = str(input("abi ")).lower()

vowelcount = 0

for char in text:
    if char in "aeiouõöäü":
        vowelcount += 1
        
print(vowelcount)        