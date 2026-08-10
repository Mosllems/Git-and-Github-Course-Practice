from datetime import datetime

user_name = input("Please enter your name: ")
user_message = input("Please enter your message: ")

if user_message == "Hello":
    print(f"Hi {user_name} How are you doing? \nIs everything on trach?")

elif user_message == "How are you?":
    print(f"Thanks! \nHow can I help you today?")

elif user_message == "What day is today?":
    print(f"Today is {datetime.today().strftime('%Y-%m-%d')}")

elif user_message == "Introduce yourself":
    print(f"I'm a mini chatbot built by Moslem Amiri")