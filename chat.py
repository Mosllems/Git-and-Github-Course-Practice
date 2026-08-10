import datetime


def get_user_name():
    user_name = input("Please enter your name: ")
    return user_name

def get_user_message():
    messages = ['hello', 'how are you?', 'what day is today?', 'what time is it?', 'introduce yourself', 'bye']
    user_message = input("Please enter your message: ")
    user_message.lower()
    if user_message not in messages:
        print("You entered a wrong input please try again!")

    return user_message


user_name = get_user_name()


while True:

    user_message= get_user_message()

    if user_message == "hello":
        print(f"Hi {user_name}\nI hope you are doing well")

    elif user_message == "how are you?":
        print(f"Thanks! \nHow can I help you today?")
        
    elif user_message == "what day is today?":
        print(f"Today is {datetime.today().strftime('%Y-%m-%d')}")

    elif user_message == "what time is it?":
        print(f"Time is {datetime.datetime.now().time().isoformat(timespec='seconds')}")
        
    elif user_message == "introduce yourself":
        print(f"I'm a mini chatbot built by Moslem Amiri")

    elif user_message == "bye":
        print(f"Bye for now {user_name}!\nI look forward to seeing you agin.")
        break
        