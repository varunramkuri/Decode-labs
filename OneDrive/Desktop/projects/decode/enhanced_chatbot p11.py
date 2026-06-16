
from datetime import datetime
import random
import string

def run_chatbot():
    print("System Boot: Hello! I am your enhanced AI assistant.")
    print("Type 'exit' to end our conversation.\n")

    tasks = []
    notes = []

    responses = {
        "hello": "Hi there! How can I help you today?",
        "hi": "Hello! What's on your mind?",
        "how are you": "I'm running smoothly, thank you!",
        "help": """
Available Commands:
- hello / hi
- status
- joke
- time
- date
- motivate
- generate password
- calc <expression>
- add task <task>
- show tasks
- note <text>
- show notes
- exit
""",
        "status": "All systems operational!",
        "joke": "Why do programmers prefer dark mode? Because light attracts bugs!"
    }

    quotes = [
        "Success comes from consistency.",
        "Keep learning every day.",
        "Small progress is still progress.",
        "Discipline beats motivation.",
        "Every expert was once a beginner."
    ]

    while True:
        user_input = input("You: ")
        clean_input = user_input.lower().strip()

        if clean_input in ["exit", "quit"]:
            print("Bot: Goodbye!")
            break

        elif "good morning" in clean_input:
            print("Bot: Good morning! Hope you have a productive day.")

        elif "thank" in clean_input:
            print("Bot: You're welcome!")

        elif "time" == clean_input:
            print("Bot:", datetime.now().strftime("%H:%M:%S"))

        elif "date" == clean_input:
            print("Bot:", datetime.now().strftime("%d-%m-%Y"))

        elif clean_input.startswith("calc "):
            try:
                expression = user_input[5:]
                result = eval(expression)
                print("Bot:", result)
            except Exception:
                print("Bot: Invalid calculation.")

        elif clean_input.startswith("add task "):
            task = user_input[9:]
            tasks.append(task)
            print("Bot: Task added.")

        elif clean_input == "show tasks":
            if tasks:
                print("Bot: Your Tasks")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
            else:
                print("Bot: No tasks available.")

        elif clean_input.startswith("note "):
            notes.append(user_input[5:])
            print("Bot: Note saved.")

        elif clean_input == "show notes":
            if notes:
                print("Bot: Your Notes")
                for i, note in enumerate(notes, 1):
                    print(f"{i}. {note}")
            else:
                print("Bot: No notes saved.")

        elif clean_input == "motivate":
            print("Bot:", random.choice(quotes))

        elif clean_input == "generate password":
            password = ''.join(
                random.choices(
                    string.ascii_letters +
                    string.digits +
                    string.punctuation,
                    k=12
                )
            )
            print("Bot:", password)

        elif "weather" in clean_input:
            print("Bot: Weather service is currently unavailable.")

        else:
            reply = responses.get(
                clean_input,
                "I do not understand. Could you rephrase that?"
            )
            print("Bot:", reply)

if __name__ == "__main__":
    run_chatbot()
