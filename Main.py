from features.code_generator import generate_code
from features.bug_fixer import fix_bug
from features.explainer import explain_code
from features.grammar import improve_english
from features.chat import chat_mode   # NEW

def main():
    while True:
        print("\n=== AI Dev Assistant ===")
        print("1. Generate Code")
        print("2. Fix Bug")
        print("3. Explain Code")
        print("4. Improve English")
        print("5. Chat with AI")   # NEW
        print("6. Exit")

        choice = input("Choose: ")

        if choice == "1":
            generate_code()
        elif choice == "2":
            fix_bug()
        elif choice == "3":
            explain_code()
        elif choice == "4":
            improve_english()
        elif choice == "5":
            chat_mode()   # NEW
        elif choice == "6":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()