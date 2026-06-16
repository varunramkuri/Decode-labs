def run_chatbot():
    print("System Boot: Hello! I am your rule-based AI assistant.")
    print("Type 'exit' to end our conversation.\n")

    # KNOWLEDGE BASE: Dictionary with 5+ intents
    # This provides O(1) constant time lookup
    responses = {
        "hello": "Hi there! How can I help you today?",
        "hi": "Hello! What's on your mind?",
        "how are you": "I'm just a logic engine running smoothly, thank you! And you?",
        "help": "I can respond to basic greetings, check my status, or tell you a joke. Try saying 'status'.",
        "status": "All systems operational. Running in constant time O(1)!",
        "joke": "Why do programmers prefer dark mode? Because light attracts bugs!",
        "bye": "Goodbye! Have a great day.",
        "goodbye": "Farewell! Shutting down..."
    }

    # INPUT LOOP: The Infinite Cycle
    while True:
        # Phase 1: Input & Sanitization
        raw_input = input("You: ")
        # Handle case & whitespace
        clean_input = raw_input.lower().strip() 
        
        # Phase 2: Exit Strategy
        # Clean break command to kill the loop
        if clean_input in ['exit', 'quit']:
            print("Bot: Terminating process. Goodbye!")
            break

        # Phase 3: Process & Output
        # Atomic Operation: Lookup + Fallback using the .get() method
        reply = responses.get(clean_input, "I do not understand. Could you rephrase that?")
        
        print(f"Bot: {reply}")

if __name__ == "__main__":
    run_chatbot()