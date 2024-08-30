import random
import time
import datetime
haxii = 0
klondike = random.randint(1, 5)
goddays = random.randint(1, 1000000)
whatwouldyou = ["let a family member choose a haircut for you", "run hack", "explode your most precious minecraft building", "sit outside in the rain", "create a useless python code",]
thehackening = ["installing linux packages...", "making movie references...", "removing unused braincells...", "installing viruses...", "waiting for what windows thinks is 42 hours...", "coding a useless terminal program in python...", "ctrl + alt + delete...", "friending spam bots...", "downloading more ram...", "watching youtube tutorials...", "subscribing to useless newsletters...", "stealing money from the rich and giving it to the poor...", "submerging your computer in mineral oil", "eating thermal paste...", "beatingsans...", "waiting for hollow knight silksong to come out...", "updating drivers...", "deleting system32...", "doxxing..."]
print("red panda OS [Version 1.02] \n(c) dragonborne corperation. no rights reserved")
while True:
    micro = input("C:/useless/terminal> ")
    if micro == "help":
        print("commands: \nhelp - prints this message \ngod - the countdown \ntime - tell the time\ntimer - create a timer \nhack - be the hacker! \nexit - its obvious")
    elif micro == "god":
        print("god is coming. " + str(goddays) + " days remain")
    elif micro == "time":
        curent = datetime.datetime.now()
        print(str(curent))
    elif micro == "timer":
        tome = input("how long to set timer> ")
        time.sleep(int(tome))
        print("timer is done")
    elif micro == "debug":
        print("printing variable values...")
        print("goddays var = " + str(goddays))
        print("micro var = " + micro)
        print("printing list lengths...")
        print("thehackening list length = " + str(len(thehackening)))
        print("debug finished \nthank you for using uselessterminal")
    elif micro == "hack":
        while (haxii < random.randint(10, 50)):
            haxor = random.randint(1, 18)
            print(thehackening[haxor])
            time.sleep(1.5)
            haxii = haxii + 1
        print("hack complete \nhacking brought to you by https://hackertyper.net ")
    elif micro == "klondike":
        print("what would you do for a klondike bar?\n" + whatwouldyou[klondike])
    elif micro == "exit":
        print("bye bye!")
        time.sleep(0.5)
        exit()