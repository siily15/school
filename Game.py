import time

answer_A = ["A","a"]
answer_B = ["B","b"]
answer_C = ["C","c"]

user_name = input("What is you name? ")
time.sleep(1)
print("Hello " + user_name)

player_type =  input("What class you want to be mage, archer and warrior ")
if player_type in "mage":
    print("You can use fire, water and air spells")
if player_type in "archer":
    print("You can use range attacks")
if player_type in "warrior":
    print("You can only use close attacks")
    
act1 = input("You ran into a monter you have to chose to fight him or run from him ")
time.sleep(1)
if act1 in "run":
    act2 = input("You ran from the monster but you ended up in a cave you see a bright ligt at the end of the cave you can go inside the cave  or run back ")
    if act2 in "run":
        print("You ran back but you ran into the same monster you ran from last time and this time he kills you ")
    if act2 in "inside":
       act3 = input("You find a hut at the end of the cave you go inside there is a men sitting on a rockin chair and he tells you to sid next to him. You sit next to him she tells you take the armor and the weapon from you class you choosed staff, sword or bow and you need to kill all the monsters who are outside the cave to save the word ")
    if act3 in "staff":
        print("You started to learn new spells and you started to level up you character when you went to fight the mosters tou killed alle of them and you saved the world ")
    if act3 in "sword":
        print("You went to fight the monster but you bearly maited out live")
    if act3 in "bow":
        print()
        
   
            
if act1 in "fight":
    print("You killed the monster but his freinds came to help him and now you are 1 acenst 10, you need to fight them all but you get killed ")