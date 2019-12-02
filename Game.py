import time


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
    act2 = input("""You ran from the monster but you ended up in a cave you see a bright ligt at the
end of the cave you can go inside the cave or run back """)
    if act2 in "run":
        print("You ran back but you ran into the same monster you ran from last time and this time he kills you ")
    if act2 in "inside":
        act3 = input("""You find a hut at the end of the cave you go inside there is a men sitting
on a rockin chair and he tells you to sid next to him.You sit next to him she tells you take the
armor and the weapon from you class you choosed staff, sword or bow and you need to kill all the
monsters who are outside the cave to save the word """)
    if act3 in "staff":
        act4 = input("""You started to learn new spells and you started to level up you character
when you went to fight the mosters you killed al of them but you did't know how to to cet pack to spawn
and now you are wontering around the map and you find a forest there are plenty of food, you find
a village inside the forest youyou go to take a closer look at the village and you find there are
a lot of embty hauses, but there is a one man who is still there and you can ignone him or ask where
all the people went? """)
    time.sleep(1)
    if act4 in "ignore":
        print("""you wonder araund the village and you pumb into that man agen but you ignore him and
move on and you leave the village and never see that man agen. """)
    if act4 in "where all the people went":
        act5 = input("""Man tells you that they went to nerby mounten so that the would be safe but they got
traped in a cave top of the mounten, you can go look for the poeple or leave the village and wonder arund the map""")
    if act5 in "look for the poeple":
        act6 = input("""You find the mounten and see the cave on topp of the mounten, you clime top of the mounten to save the village people
 but most of them are dead becuse they didnt have so much food and water whith them, but most of them are alive they cant get out because
 there are a lot of monster nerby. You can go back or figt the mosters""")
    if act6 in "go back":
        print()
    if act5 in "leave the village":
        print("""You leave the village and you found a heling well and you heal all your wounds and them you find a spawn you saved the world,
but you rembeberd the village people fo were missing from the village and you go and ask the man where are the village people  """)
        
    if act3 in "sword":
        print("You went to fight the monster but you bearly maited out live")
    if act3 in "bow":
        print()           
if act1 in "fight":
    print("You killed the monster but his freinds came to help him and now you are 1 acenst 10, you need to fight them all but you get killed ")
