
version = 1.0
channel = "stable"
codename = "Antiquity"

print(f"\nIssOS {version} {channel} {codename}")
print("By: Issah Abeebllahi Issah")

while True:
    choice = input("""
    1. I have used IssOs before
    2. I am a new user
    """)
    if choice == "1":
        username_file = open("data/username.info", "r").read()
        password_file = open("data/password.info", "r").read()

        print("Hi " + username_file + "!")
        password = input("\nWhat is your password: ")

        if password_file == password:
            exec(open("os.py").read())
        else:
            print("Wrong password!")
    if choice == "2":
        username = input("\nWhat is your username: ")
        password = input("What is your password: ")

        username_file = open("data/username.info", "w")
        password_file = open("data/password.info", "w")

        username_file.write(username)
        password_file.write(password)
        exec(open("os.py").read())