from PIL import Image
import platform
import datetime
import time
import random
from rich.console import Console
import requests
version = "v0.1"
console = Console()
console.print("run [u]help[/u] for help")
while True:
    inp = input("> ")
    if inp == "timeis":
        timis = datetime.datetime.now()
        console.print(f"Current time is: [bold sky_blue2]{timis}[/bold sky_blue2]")
    elif inp == "quit":
        console.print("[bold grey63]Quitting in 5 seconds...[/bold grey63]")
        time.sleep(5)
        exit()
    elif inp == "pyfetch":
        with console.status("fetching...", spinner="line"):
            fetcher = platform.uname()
            time.sleep(0.5)
            pfetchr = platform.python_version
            console.rule("fetch results")
            console.print(f"[dodger_blue1]System:[/dodger_blue1] {fetcher.system} ")
            console.print(f"[dodger_blue1]Node Name:[/dodger_blue1] {fetcher.node} ")
            console.print(f"[dodger_blue1]Release:[/dodger_blue1] {fetcher.release} ")
            console.print(f"[dodger_blue1]Version:[/dodger_blue1] {fetcher.version} ")
            time.sleep(0.5) # to emulate hyfetch lag cause why not honestly
            console.print(f"[dodger_blue1]Machine:[/dodger_blue1] {fetcher.machine} ")
            console.print(f"[dodger_blue1]Processor:[/dodger_blue1] {fetcher.processor} ")
    elif inp == "help":
        print("use help -c [command] to get help for that specific command")
        console.rule("commands")
        print("help - this command \ntimeis - gives you the time \npyfetch - neofetch but worse \nquit - quits boop")
    elif inp.startswith("help -c ") == True:
        hc = inp.replace("help -c ", "")
        if hc == "timeis":
            print("Tells you your systems time\nNo arguments")
        elif hc == "pyfetch":
            print("Tells you system information\nNo arguments")
        elif hc == "run":
            print("runs a feature that you cant exit without exiting boop itself\n'subapp' - the feature to run")
        else:
            console.print("[bold red]ERROR: [/bold red]either thats not a command or you spelt something wrong")
    elif inp.startswith("run ") == True:
        subapp = inp.replace("run ", "")
        if subapp == "RBTXTE":
            while True:
                print("rbtxte lite \nfilenames must end in .txt")
                print("edit or read")
                chos = input('> ')
                if chos == "read":
                    print("input filename")
                    filena = input('> ')
                    try:
                        red = open(filena)
                        print(red.read())
                    except FileNotFoundError:
                        print("file not found")
                    except PermissionError:
                        print("access denied")
                elif chos == "write":
                    print("input filename")
                    filena = input('> ')
                    print("input text for file")
                    filetx = input('> ')
                    try:
                         open(filena, 'a').write.filetx
                    except FileNotFoundError:
                        print("file not found")
                    except PermissionError:
                        print("access denied")
                elif chos == "quit":
                    print("quitting now")
                    exit()