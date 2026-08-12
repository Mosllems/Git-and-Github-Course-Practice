def user_message():
    print("Welcome, Please Choose your operation and enter your numbers...")
    print("Addition, Subtraction, Multiplication, Division")

    user_operation = input("Please enter your operation: ")
    user_operation = user_operation.lower()

    try:
        first_number = int(input("Please enter your first number: "))
        second_number = int(input("Please enter your second number: "))

        if user_operation == "addition":
            return first_number + second_number

        elif user_operation == "subtraction":
            return first_number - second_number

        elif user_operation == "multiplication":
            return first_number * second_number

        elif user_operation == "division":
            return first_number / second_number

    except ValueError:
        print("You entered a wrong input. Please try again...")


print(user_message())