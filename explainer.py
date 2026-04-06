from utils.api_client import ask_ai

def explain_code():
    code = input("\nPaste code to explain:\n")

    prompt = f"""
    Explain this code in simple terms:

    {code}
    """

    result = ask_ai(prompt)

    print("\n🧠 Explanation:\n")
    print(result)