import time


user_name = input("What is you name? ")
time.sleep(1)
print("Hello " + user_name)

player_type =  input("What class you want to be mage, archer and warrior:  ")
if player_type in "mage":
    print("You can use fire, water and air spells")
if player_type in "archer":
    print("You can use range attacks")
if player_type in "warrior":
    print("You can only use close attacks")
    
act1 = input("You ran into a monter you have to chose to fight him or run from him:  ")
time.sleep(1)
if act1 in "run":
    act2 = input("""You ran from the monster but you ended up in a cave you see a bright ligt at the
end of the cave you can go inside the cave or run back:  """)
    if act2 in "run":
        print("You ran back but you ran into the same monster you ran from last time and this time he kills you:  ")
    if act2 in "inside":
        act3 = input("""You find a hut at the end of the cave you go inside there is a men sitting
on a rockin chair and he tells you to sid next to him.You sit next to him she tells you take the
armor and the weapon from you class you choosed staff, sword or bow and you need to kill all the
monsters who are outside the cave to save the word:  """)
    if act3 in "staff":
        act8 = input("""You started to learn new spells and you started to level up you character
when you went to fight the mosters you killed al of them but you did't know how to to cet pack to spawn
and now you are wontering around the map and you find a forest there are plenty of food, you find
a village inside the forest youyou go to take a closer look at the village and you find there are
a lot of embty hauses, but there is a one man who is still there and you can ignone him or ask where
all the people went? """)
    if act3 in "sword":
        print("You went to fight the monster but you bearly maited out live")
    if act3 in "bow":
       act4 = input("""You started to kill mosters but you ran out of arrows in you quiver, you can make more or you can buy from market buy
 you can only afford least 10: """)
    if act4 in "buyfrom market":
        print("You bught new arrows but you needed more mone to buy some more and now you need to help the shopkeeper you have a choise to defend his shop or clean for him")
    if act4 in "make more":
        act5 = input("""You started to make more but you failed on you first one but you got better on you second one and now you started make petter wons and you satrted to sell them
so that you can make money you went to kill more monster an you found a new bow from a chest but it was a but broken you could repair you new or you could use youre old one: """)
    if act5 in "repair":
        print("""You started to repair you new but you saw monsters coming from forest and you craped ypu oled one but it broke in half and you needed to fix you new bow fast but you didnt 
have that time to fix you new one, you needed to run a nerby cave when you fixed your new bow you started to kill all the moster fo came from the forest and you ran out of arrows agen  : """)           
    if act1 in "fight":
        print("You killed the monster but his freinds came to help him and now you are 1 acenst 10, you need to fight them all but you get killed ")
    time.sleep(1)
    if act8 in "ignore":
        print("""you wonder araund the village and you pumb into that man agen but you ignore him and
move on and you leave the village and never see that man agen:  """)
    if act8 in "where all the people went":
        act6 = input("""Man tells you that they went to nerby mounten so that the would be safe but they got
traped in a cave top of the mounten, you can go look for the poeple or leave the village and wonder arund the map: """)
    if act6 in "look for the poeple":
        act7 = input("""You find the mounten and see the cave on topp of the mounten, you clime top of the mounten to save the village people
 but most of them are dead becuse they didnt have so much food and water whith them, but most of them are alive they cant get out because
 there are a lot of monster nerby. You can go back or figt the mosters: """)
    if act7 in "go back":
        print()
    if act7 in "leave the village":
        print("""You leave the village and you found a heling well and you heal all your wounds and them you find a spawn you saved the world,
but you rembeberd the village people fo were missing from the village and you go and ask the man where are the village people:  """)  
    if act3 in "sword":
        print("You went to fight the monster but you bearly maited out live")
    if act3 in "bow":
       act4 = input("""You started to kill mosters but you ran out of arrows in you quiver, you can make more or you can buy from market buy
 you can only afford least 10: """)
    if act4 in "buyfrom market":
        print("You bught new arrows but you needed more mone to buy some more and now you need to help the shopkeeper you have a choise to defend his shop or clean for him")
    if act4 in "make more":
        act5 = input("""You started to make more but you failed on you first one but you got better on you second one and now you started make petter wons and you satrted to sell them
so that you can make money you went to kill more monster an you found a new bow from a chest but it was a byt brogen you could rebeare you new or you your old one""")           
if act1 in "fight":
    print("You killed the monster but his freinds came to help him and now you are 1 acenst 10, you need to fight them all but you get killed ")
