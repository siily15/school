input1 = input("Numbrid: ")

numbers = input1.split(", ")

print("Sisend: "+ str(numbers))

numbers2 = [numbers[0], numbers[-1]]
print ("Väljund: " + str(numbers2))