from utils.api_client import ask_ai

def generate_code():
    question = input("\nEnter your coding question: ")

    prompt = f"""
    Give ONLY code.
    No explanation.
    Clean and runnable.

    Question:
    {question}
    """

    result = ask_ai(prompt)

    print("\n💻 Generated Code:\n")
    print(result)