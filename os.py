import sys

version = (1, 0, 3)

print("\nWelcome to Iss OS!")

def sysinfo():
    print(f"\nIssOS {version}")
    print("By: Issah Abeebllahi Issah")

def exit():
    sys.exit()

while True:
    print("\nWhat do you want to run?")
    print("exit")
    print("sysinfo\n")
    command = input()

    #System info
    if command == "sysinfo":
        sysinfo()
    
    #Exit
    if command == "exit":
        exit()