import time
version = "multitool v0.1 "
utilist = "timer \ncalculator \nRBTXTElite"
pnum = "(please only input numbers)"
inp = '> '
while True:
    print("wellcome to " + version)
    print("options: utilities, and games")
    cmd = input(inp)
    if cmd == "utilities":
        print("choose a utility")
        print(utilist)
        choice = input(inp)
        if choice == "timer":
            print("how many seconds to set timer for?")
            print(pnum)
            timeo = input(inp)
            imte = int(timeo)
            print("timer set for " + timeo + " seconds")
            time.sleep(imte)
            print("timer finished!")
        elif choice == "calculator":
            print("input first number")
            print(pnum)
            num0 = input(inp)
            num1 = int(num0)
            print("input second number")
            print(pnum)
            num00 = input(inp)
            num2 = int(num00)
            print("input calculator mode")
            print("addition(+) \nsubtraction(-) \nmultiplication(*) \ndevision(/) \nexponents(^)")
            mode = input(inp)
            if mode == "+" or "addition":
                outp = num1+num2
                uotput = str(outp)
                print("awnser is " + uotput)
            elif mode == "-" or "subtraction":
                outp = num1-num2
                uotput = str(outp)
                print("awnser is " + uotput)
            elif mode == "*" or "multiplication":
                outp = num1*num2
                uotput = str(outp)
                print("awnser is " + uotput)
            elif mode == "/" or "devision":
                outp = num1/num2
                uotput = str(outp)
                print("awnser is " + uotput)
            elif mode == "^" or "exponents":
                outp = num1**num2
                uotput = str(outp)
                print("awnser is " + uotput)
            else:
                print("either thats not a supported option or you put something in wrong")
        elif choice == "RBTXTElite":
            print("RBTXTE lite \nfilenames must end in .txt")
            print("edit or read")
            chos = input(inp)
            if chos == "read":
                print("input filename")
                filena = input(inp) 
                try:
                    reed = open(filena)
                    print(reed.read())
                except FileNotFoundError:
                    print("file not found")
                except PermissionError:
                    print("access denied")
            elif chos == "edit":
                print("input filename")
                filena = input(inp)
                print("input file text")
                filetx = input(inp)
                try:
                    open(filena, 'a').write(filetx)
                except FileNotFoundError:
                    print("file not found")
                except PermissionError:
                    print("access denied")       
    elif cmd == "games":
         print("no games available at the moment, but that could change any update!")
    
    