# main.py (Fully Fixed & Interactive AI Chatbot)
import tkinter as tk
from tkinter import scrolledtext, simpledialog, messagebox
from chatbot_engine import responsetochatbot, motivation_reply, study_help_reply
import datetime

# -------------------- Create main window --------------------
root = tk.Tk()
root.title("AI Chatbot")
root.geometry("700x500")

# Chat display (read-only)
chat_display = scrolledtext.ScrolledText(root, width=80, height=20, state='disabled', wrap=tk.WORD)
chat_display.pack(pady=10)

# Mode selection
mode_var = tk.StringVar(value="Normal Chat")
mode_menu = tk.OptionMenu(root, mode_var, "Normal Chat", "Motivation", "Study Help")
mode_menu.pack(side='left', padx=5, pady=5)

# Entry widget for user input
user_input = tk.Entry(root, width=50)
user_input.pack(side='left', padx=10, pady=5)

# -------------------- Global state --------------------
waiting_for_motivation_answer = False  # Waiting for Yes/No to quote
last_was_motivation = False           # To respond politely if user says thanks

# -------------------- Greeting Feature --------------------
present_time = datetime.datetime.now().hour

# Ask for user name safely
name = simpledialog.askstring("Name", "Enter your name:")
if not name:  # handle cancel or empty input
    name = "User"

# Determine greeting based on time
if 5 <= present_time < 12:
    greeting = f"GOOD MORNING, {name}!"
elif present_time == 12:
    greeting = f"GOOD NOON, {name}!"
elif 13 <= present_time < 16:
    greeting = f"GOOD AFTERNOON, {name}!"
elif 16 <= present_time <= 20:
    greeting = f"GOOD EVENING, {name}!"
else:
    greeting = f"GOOD NIGHT, {name}! SWEET DREAMS!"

# Show greeting in chat display
chat_display.config(state='normal')
chat_display.insert(tk.END, f"Bot: {greeting}\n")
if mode_var.get() == "Normal Chat":
    chat_display.insert(tk.END, "Bot: Please ask me a question or type anything to chat.\n")
chat_display.config(state='disabled')

# -------------------- Thank you messages --------------------
thank_you_msgs = ["thank you", "thanks", "aww thank you", "thankyou", "thx", "thank u"]

# -------------------- Function to save chat --------------------
def save_chat(user_msg, bot_msg, end_chat=False):
    try:
        with open("chathistory.txt", "a", encoding="utf-8") as f:
            f.write(f"User: {user_msg}\n")
            f.write(f"Bot: {bot_msg}\n")
            if end_chat:
                f.write("---- Chat Ended ----\n\n")
            else:
                f.write("\n")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save chat: {e}")

# -------------------- Function to send message --------------------
def send_message():
    global waiting_for_motivation_answer, last_was_motivation

    message = user_input.get().strip()
    if message == "":
        return
    user_input.delete(0, tk.END)

    # Show user message
    chat_display.config(state='normal')
    chat_display.insert(tk.END, f"You: {message}\n")
    chat_display.config(state='disabled')
    chat_display.yview(tk.END)

    # Check for exit
    if message.lower() == "bye":
        bot_reply = "Bye! Have a nice day."
        chat_display.config(state='normal')
        chat_display.insert(tk.END, f"Bot: {bot_reply}\n")
        chat_display.config(state='disabled')
        chat_display.yview(tk.END)
        save_chat(message, bot_reply, end_chat=True)
        root.destroy()
        return

    # ---------------- Polite response after motivational quote ----------------
    if last_was_motivation and message.lower() in thank_you_msgs:
        bot_reply = "It's my pleasure! 😊"
        last_was_motivation = False
        chat_display.config(state='normal')
        chat_display.insert(tk.END, f"Bot: {bot_reply}\n")
        chat_display.config(state='disabled')
        chat_display.yview(tk.END)
        save_chat(message, bot_reply)
        return

    # Check current mode
    mode = mode_var.get()

    # ---------------- Motivation Mode ----------------
    if mode == "Motivation":
        if waiting_for_motivation_answer:
            if message.lower() in ["yes", "y"]:
                bot_reply = motivation_reply()
                last_was_motivation = True
            else:
                bot_reply = "Okay, maybe next time!"
                last_was_motivation = False
            waiting_for_motivation_answer = False
        else:
            bot_reply = "Do you want a motivational quote? (Yes/No)"
            waiting_for_motivation_answer = True
            chat_display.config(state='normal')
            chat_display.insert(tk.END, f"Bot: {bot_reply}\n")
            chat_display.config(state='disabled')
            chat_display.yview(tk.END)
            save_chat(message, bot_reply)
            return

    # ---------------- Study Help Mode ----------------
    elif mode == "Study Help":
        bot_reply = study_help_reply()
        last_was_motivation = False

    # ---------------- Normal Chat Mode ----------------
    else:
        bot_reply = responsetochatbot(message)
        last_was_motivation = False
        if not bot_reply:
            teach = messagebox.askyesno("Teach Bot", "I am not aware of this question. Can you teach me?")
            if teach:
                new_answer = simpledialog.askstring("Teach Bot", "Enter correct answer:")
                if new_answer:
                    bot_reply = new_answer
                    try:
                        with open("learned_data.txt", "a", encoding="utf-8") as f:
                            f.write(f"{message.lower()}::{new_answer}\n")
                    except Exception as e:
                        messagebox.showerror("Error", f"Failed to save learned data: {e}")
                else:
                    bot_reply = "Okay, I will skip this."
            else:
                bot_reply = "Okay, I will skip this."

    # Show bot reply
    chat_display.config(state='normal')
    chat_display.insert(tk.END, f"Bot: {bot_reply}\n")
    chat_display.config(state='disabled')
    chat_display.yview(tk.END)

    # Save chat history
    save_chat(message, bot_reply)

# -------------------- Send button --------------------
send_button = tk.Button(root, text="Send", width=10, command=send_message)
send_button.pack(side='left', padx=5, pady=5)

# Bind Enter key to send message
root.bind('<Return>', lambda event: send_message())

# -------------------- Run GUI --------------------
root.mainloop()




