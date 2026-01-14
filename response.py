# add responses 
responses = {
    "hello": "Hello! How can I help you?",
    "how are you": "I am great! What about you?",
    "i am fine": "Great to hear that!",
    "what is your name": "I am your AI Chatbot.",
    "who are you": "I am an AI smart chatbot created in Python.",
    "tell me about python": "Python is a beginner-friendly programming language."
}

# load learned data from file (if exists)
try:
    with open("learned_data.txt", "r") as file:
        for line in file:
            q, a = line.strip().split("::")
            responses[q] = a
except FileNotFoundError:
    pass

# add function 
def responsetochatbot(userquestion):
    userquestion = userquestion.lower().strip()
    if userquestion in responses:
        return responses[userquestion]
    return None

def show_menu():
    print("\nChoose a mode:")
    print("1. Normal Chat")
    print("2. Motivation Mode")
    print("3. Study Help Mode")
    print("4. Exit")

def motivation_reply():
    quotes = [
        "Believe in yourself. You are stronger than you think.",
        "Every day is a new chance to grow.",
        "Small steps today lead to big success tomorrow.",
        "Don't give up. Your future is bright."
    ]
    import random
    return random.choice(quotes)

def study_help_reply():
    tips = [
        "Make a daily study schedule and follow it.",
        "Revise what you learn the same day.",
        "Practice coding daily, even for 30 minutes.",
        "Break big topics into small parts."
    ]
    import random
    return random.choice(tips)

# main loop
while True:
    show_menu()
    mode = input("Enter your choice (1-4): ")

    if mode == "4":
        print("Bot: Goodbye! Keep learning.")
        break

    elif mode == "2":
        print("\n--- Motivation Mode ---")
        print("Bot:", motivation_reply())

    elif mode == "3":
        print("\n--- Study Help Mode ---")
        print("Bot:", study_help_reply())

    elif mode == "1":
        print("\n--- Normal Chat Mode ---")
        print("Type your question or 'exit' to go back to the menu.")
    else:
        print("This no of menu doesnot exist")

        while True:
            userquestion = input("You: ").strip()
            
            if userquestion.lower() == "exit":
                print("Bot: Exiting Normal Chat Mode.")
                break
            elif userquestion.lower() == "bye":
                reply = "Bye! Have a nice day."
                print("Bot:", reply)
                with open("chat_history.txt", "a") as file:
                    file.write(f"User: {userquestion}\nBot: {reply}\n---- Chat Ended ----\n\n")
                exit()  # fully exit the program

            # normal chat responses
            reply = responsetochatbot(userquestion)
            if reply:
                print("Bot:", reply)
            else:
                print("I am not aware about this question, can you teach me?")
                choice = input("Type yes or no: ").lower()
                if choice == "yes":
                    new_answer = input("Enter correct answer: ")
                    responses[userquestion.lower()] = new_answer
                    with open("learned_data.txt", "a") as file:
                        file.write(f"{userquestion.lower()}::{new_answer}\n")
                    print("Bot: Thank you! I have learned this.")
                    reply = new_answer
                else:
                    reply = "Okay, I will skip this."
                    print("Bot:", reply)

            # save chat history
            with open("chat_history.txt", "a") as file:
                file.write(f"User: {userquestion}\nBot: {reply}\n\n")
