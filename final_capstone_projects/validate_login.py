match = False

user = {"phelix" : "password123", "jenny" : "passw0rd"}

while not match:
    username = input("\nWhat's your username? ").lower()
    password = input("\nWhat's your password? ")
    if username not in user:
        print("This is not a registered username.")
        continue
    elif password != user[username]:
        print("Wrong password")
        continue
    elif password == user[username]:
        print(f"Hi {username}")
        match = True

print("Username and Password validated")