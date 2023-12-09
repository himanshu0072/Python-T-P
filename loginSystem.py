users = [
    {"username": "user1", "password": "pass1", "attempts": 0},
    {"username": "user2", "password": "pass2", "attempts": 0},
    {"username": "user3", "password": "pass3", "attempts": 0}
]

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    for user in users:
        if user["username"] == username:
            if user["password"] == password:
                print("Login successful!")
                user["attempts"] = 0
                return
            else:
                user["attempts"] += 1
                print("Wrong password!")
                if user["attempts"] >= 3:
                    print("Too many wrong attempts. Account locked.")
                    return
            break
    else:
        print("Invalid username!")
        return

login()
