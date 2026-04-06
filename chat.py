from utils.api_client import ask_ai

def chat_mode():
    print("\n💬 Chat Mode (type 'exit' to quit)\n")

    history = ""

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        # maintain conversation context
        history += f"\nUser: {user_input}\nAI:"

        response = ask_ai(history)

        print("\nAI:", response)

        history += response