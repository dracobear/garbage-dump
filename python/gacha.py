import random
ranks = ["broken", "common", "rare", "uncommon", "super rare", "ULTIMATE"]
objects = ["table lamp", "pool noodle", "dice", "candle", "ketchup", "yarn ball", "sunflower"]
while True:
    rank =  random.choice(ranks)
    objec = random.choice(objects)
    press = input("press enter to draw! ")
    output = objec    
    if press == "test":
        print(ranks)
        print(objects)
    else:
        print(rank + " " + output)
