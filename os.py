import sys

version = (1, 0, 1)

print("\nWelcome to Iss OS!")

def sysinfo():
    print(f"\nIssOS {version}")
    print("By: Issah Abeebllahi Issah")

def exit():
    sys.exit()

while True:
    print("\nWhat do you want to run?")
    print("e: exit")
    print("i: system info\n")
    command = input()

    #System info
    if command == "i":
        sysinfo()
    
    #Exit
    if command == "e":
        exit()