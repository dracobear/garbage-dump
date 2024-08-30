import random
intcount = 0
print("only ask yes or no questions! \nsay npc for how npc's act \nif something doesnt make sense, or you cant figure it out, ignore it \nto avoid overspecificness, you can sometimes ask if everything is as expected \nif no say unexpect")
while True:
    die = random.randint(1, 6)
    dead = random.randint(1,10)
    huh = input("what do you ask the autodm? \n")
    if die == 1:
        print("no, and...")
    elif die == 2:
        print("no.")
    elif die == 3:
        print("no, but...")
    elif die == 4:
        print('yes, but...')
    elif die == 5:
        print("yes.")
    elif die == 6:
        print("yes, and...")
        intcount = intcount + 1
    if intcount == 3:
        intcount = 0
        print("its time for a change!")
        if die == 1:
            print("a new entity appears")
        elif die == 2:
            print("something good happens to an allready exsisting entity")
        elif die == 3:
            print("something bad happens to an allready exsisting entity")
        elif die == 4:
            print("something good happens to you")
        elif die == 5:
            print('something bad happens to you')
        elif die == 6:
            print("ask https://wordcounter.net/random-word-generator for two random words")
    if huh == "npc":
        if die == 1 or 2:
            print("the npc is hostile towards you")
        elif die == 3 or 4:
            print("the npc is neutral towards you")
        elif die == 5 or 6:
            print("the npc is friendly towards you")
    elif huh == "unexpect":
        if dead == 1:
            print("something very minor is increased")
        elif dead == 2:
            print("something very minor is decreased")
        elif dead == 3:
            print("something very minor is added")
        elif dead == 4:
            print("something very minor is removed")
        elif dead == 5:
            print("something major is increased")
        elif dead == 6:
            print("something major is decreased")
        elif dead == 7:
            print("something major is added")
        elif dead == 8:
            print("something major is removed")
        elif dead == 9 or 10:
            print("ask https://wordcounter.net/random-word-generator for two random words")