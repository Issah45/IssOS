import sys

version = 1.0
channel = "stable"
codename = "Antiquity"

print("\nWelcome to Iss OS!")

def sysinfo():
    print(f"\nIssOS {version} {channel} {codename}")
    print("By: Issah Abeebllahi Issah")

def exit():
    sys.exit()

while True:
    print("""
    What do you want to run?
    e: exit
    i: system info
    """)
    command = input()

    #System info
    if command == "i":
        sysinfo()
    
    #Exit
    if command == "e":
        exit()