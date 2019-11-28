used_letters =()
word = "Ametikool"
guessed_word =["_,_,_,_,_,_,_,_,"]

letters = list(word)

while True:
    print(guessed_word)
    print("used letters" + str(used_letters))
    letter = input("Type a letter: ")
    used_letters.append(letter)
    
if letter.lower in word.lower():
    letter == word
    

    print()