from config import *
from definieren import *
from tor import *


print("  ____              _____                                    ____    _           _            	")
print(" | __ )   _   _    |_   _|  _ __   _   _  __  __ __  __     / ___|  | |__     __| | __      __	")
print(" |  _ \  | | | |     | |   | '__| | | | | \ \/ / \ \/ /     \___ \  | '_ \   / _` | \ \ /\ / /	")
print(" | |_) | | |_| |     | |   | |    | |_| |  >  <   >  <   _   ___) | | | | | | (_| |  \ V  V / 	")
print(" |____/   \__, |     |_|   |_|     \__, | /_/\_\ /_/\_\ (_) |____/  |_| |_|  \__,_|   \_/\_/  	")
print("          |___/                    |___/                                                      	")


time.sleep(1)
while (1):
    command = input(str(" Command >> "))

    if command == "ddos":
        target = input("   Target >> ")
        threads = input("   Threads >> ")
        timer = input("    Time >> ")
        os.system("cd C:/Users/Leon/Desktop/HackingTools/Scriptpy/DDoSTool/")
        os.system("python main.py" + " " + target + " " + threads + " " + timer)

    elif command == "ytbot":
        ytbot()

    elif command == "passgen":
        passgen()

    elif command == "help":
        print("Commands :")
        print("     #passgen")
        print("     #ddos")
        print("     #ytbot")
        print("     #skribblbot")
        print("     #ytviewbot")

    elif command == "skribblbot":
        tor()
        skribblbot()
        tor()
    elif command == "backdoor":
        backdoor()

    elif command == "ytviewbot":
        ytviewbot()

    else:
        print("~ Failed Try it again!")
