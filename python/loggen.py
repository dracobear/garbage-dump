import time
from datetime import datetime
rightnow = datetime.now()
print("Wellcome to log gen \nthe log generator by draco")
while True:
    print("who was the person?")
    name = input("> ")
    print("any ID? \npress enter if none")
    idd = input("> ")
    print("name details satisfied")
    time.sleep(0.5)
    print("what was the violation?")
    violet = input("> ")
    print("violation details satisfied")
    time.sleep(0.5)
    print("now lets talk about you")
    print("what is your name?")
    namem = input("> ")
    print("any ID?\nsame as before, just press enter if none")
    iddd = input("> ")
    print("all details have been entered, generating log...")
    time.sleep(0.5)
    print("log generated")
    print("**VIOLATION LOG**\nuser : " + name + "(" + str(idd) + ") \nviolation: " + violet + "\ndetails filled by: " + namem + "(" + str(iddd) + ")" "\nlog generated on: " + str(rightnow))