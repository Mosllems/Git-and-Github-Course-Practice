def login(u, p):
    while True:
        username = input("Please enter your username: ")
        password = int(input("Please enter your password: "))

        if username == u and password == p:
            print("Welcome to the application!")
            break
        else:
            print("You entered wrong username or password try again...")


login("amir", 456)

