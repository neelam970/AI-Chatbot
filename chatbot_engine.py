# chatbot_engine.py

# -------------------- Responses Dictionary --------------------
responses = {
    "hello": "Hello! How can I help you?",
    "hi": "Hi there! How are you?",
    "how are you": "I am great! What about you?",
    "i am fine": "Great to hear that!",
    "what is your name": "I am your AI Chatbot.",
    "who are you": "I am an AI smart chatbot created in Python.",
    "tell me about python": "Python is a beginner-friendly programming language.",
    "who made you": "I was crafted with love and Python magic by Neelam Kumari! 💻✨",
    "who created you": "I am proudly created by Neelam Kumari, a passionate coder and AI enthusiast.",
    "who is your creator": "I popped into existence thanks to the amazing skills of Neelam Kumari! 🤖🌟"
}

# -------------------- Load learned questions & answers safely --------------------
try:
    with open("learned_data.txt", "r") as file:
        for line in file:
            line = line.strip()
            if "::" in line:
                q, a = line.split("::", 1)  # split only on first ::
                responses[q.lower()] = a
except FileNotFoundError:
    pass

# -------------------- Functions --------------------
def responsetochatbot(user_question):
    """
    Return bot response if known, else None
    """
    user_question = user_question.lower().strip()
    return responses.get(user_question, None)

def motivation_reply():
    """
    Return a random motivational quote
    """
    import random
    quotes = [
        "Believe in yourself. You are stronger than you think. ✨",
        "Every day is a new chance to grow. 💪",
        "Small steps today lead to big success tomorrow. 🌱",
        "Don't give up. Your future is bright. 🌟",
        "Dream it. Wish it. Do it! 🚀"
    ]
    return random.choice(quotes)

def study_help_reply():
    """
    Return a random study tip
    """
    import random
    tips = [
        "Make a daily study schedule and follow it.",
        "Revise what you learn the same day.",
        "Practice coding daily, even for 30 minutes.",
        "Break big topics into small parts.",
        "Take short breaks while studying to improve focus."
    ]
    return random.choice(tips)

