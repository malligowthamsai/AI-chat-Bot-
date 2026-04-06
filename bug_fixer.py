from utils.api_client import ask_ai

def fix_bug():
    code = input("\nPaste your buggy code:\n")

    prompt = f"""
    Fix the following code.
    Return only corrected code.
    No explanation.

    Code:
    {code}
    """

    result = ask_ai(prompt)

    print("\n🛠 Fixed Code:\n")
    print(result)