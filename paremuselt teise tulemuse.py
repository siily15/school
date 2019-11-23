list1 = [2, 3, 6, 6, 5]

list1 = list(dict.fromkeys(list1))
list1.sort()
print("Väljund: ", list1[-2])
