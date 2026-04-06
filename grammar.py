from utils.api_client import ask_ai

def improve_english():
    text = input("\nEnter sentence:\n")

    prompt = f"""
    Correct grammar and improve sentence:

    {text}
    """

    result = ask_ai(prompt)

    print("\n✍️ Improved:\n")
    print(result)