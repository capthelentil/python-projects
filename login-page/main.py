# Simple user database
users = {}

def register():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if username in users:
        print("This username is already in use.")
    else:
        users[username] = password
        print("Registration successful.")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if username in users and users[username] == password:
        print("Login successful.")
    else:
        print("Incorrect username or password.")

while True:
    print("\n1. Register")
    print("2. Log In")
    print("3. Exit")
    
    choice = input("Choose the operation you want to perform: ")
    
    if choice == '1':
        register()
    elif choice == '2':
        login()
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid option. Please try again.")
