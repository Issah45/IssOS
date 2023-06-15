import sys

version = 2.1
channel = "lts"
codename = "Changer"

print("\nWelcome to Iss OS!")

def sysinfo():
    print(f"\nIssOS {version} {channel} {codename}")
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