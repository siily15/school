name = str.capitalize(input('Whas is you name? '))
print('Hello ' + name)
location = str.capitalize(input('Where do you live? '))
if location == 'Saaremaa':
    print('Saaremaa is nice place to live ')
elif location == 'Pärnu':
    print('Pärnu is a nice place in summer')
age = input('How old are you? ')
if age < '18' :
    print('You are old enough to dive a car ')
elif age == '18':
    print('You can make drivers licenses ')
elif age > '18':
    print('You can now drive a car when you have driver licenses ')
