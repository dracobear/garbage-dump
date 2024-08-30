import random
randor = random.randint(0, 36)
randoj = random.randint(1,11)
name = input("enter name ")
print("your name is " + name)
mone = input("input starting money ")
money = int(mone)
print("you will start with " + mone +"$")
print("games include: \nroulette \nblackjack")
while True:
    moner = str(money)
    print ("current money = " + moner +"$")
    gamemode = input("what game would you like to play? ")
    if gamemode == "roulette":
        bet = input("how much do you bet? ")
        beter = int(bet)
        wher = input("what space do you bet one (0 - 36)")
        if wher == randor:
            bot = beter * 2
            bat = int(bot)
            print("you won " + bat +"$")
            money = money + bot
        if wher != randor:
            print('you lost...')
            money = money - beter
    if gamemode == "blackjack":
        bet = input("how much do you bet? ")
        beter = int(bet)
        hand = 0
        enhand = 0
        stand = False
        while hand < 22 or stand == False:
            hond = str(hand)
            print(hond)
            act = input("hit or stand? ")
            enhand = enhand + randoj
            if act == "hit":
                hand = hand + randoj
            elif act == "stand":
                stand = True
            else:
                print("what are you doing!")
        if hand == 21:
            bot = beter * 2
            bat = str(bot)
            print("blackjack victory!, you won" + bat + "$")
            money = money + bot
        elif hand >= 22:
            print("bust, you lost...")
            money = money - beter
        elif hand < enhand:
            print("you lost...")
            money = money - beter

        