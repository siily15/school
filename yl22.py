from random import randint

t = ["rock", "paper", "siccors"]
computer =t[randint(0,2)]
player= False


while player == False:
    player = input("rock, paper, scissors? " )   

    if player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
            
    elif player == "paper":
        if computer == "scissors":
            print("You lose")
        else:
            print("You win")
            
    elif player == "scissors":
        if computer == "rock":
            print("You lose")
        else:
            print("You win")
    else:
        print("That's not a valid play, check you spelling!")
        
    player = False
    player_1=input("To you wanna paly more?(y/n)")
    
    if player == "y":
        player = False
        computer =t[randint(0,2)]
    elif player == "n":
        exit()
    else:
        print("Good bye")