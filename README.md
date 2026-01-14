# AI Chatbot (Python + Tkinter)

This is a desktop-based AI Chatbot built using **Python** and **Tkinter**.  
It provides an interactive GUI where users can chat with the bot in different modes.

## Features
- Time-based greeting (Morning, Afternoon, Evening, Night)
- Three chat modes:
  - **Normal Chat** – General conversation with learning ability
  - **Motivation** – Polite motivational quotes
  - **Study Help** – Study-related assistance
- Chat history is saved in `chathistory.txt`
- Bot can **learn new answers** and store them in `learned_data.txt`
- Simple and user-friendly interface

## Technologies Used
- Python
- Tkinter (GUI)
- File Handling

## How It Works
- Tkinter creates the GUI (window, chat area, input box, buttons, dropdown).
- When the user sends a message, `send_message()` is triggered.
- Based on the selected mode, the message is processed by:
  - `responsetochatbot()` – Normal Chat
  - `motivation_reply()` – Motivation
  - `study_help_reply()` – Study Help
- The bot reply is displayed and saved in a file.

## How to Run
1. Make sure Python is installed.
2. Clone this repository:
   ```bash
   git clone https://github.com/neelam970/AI-Chatbot.git
