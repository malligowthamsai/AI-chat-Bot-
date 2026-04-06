import tkinter as tk
from tkinter import ttk, scrolledtext
from utils.api_client import ask_ai

# 🧠 Function to handle actions
def run_action():
    user_input = input_box.get("1.0", tk.END).strip()
    feature = feature_var.get()

    if not user_input:
        output_box.insert(tk.END, "⚠️ Please enter something\n")
        return

    if feature == "Generate Code":
        prompt = f"""
        Give ONLY code.
        No explanation.
        Clean and runnable.

        Question:
        {user_input}
        """

    elif feature == "Fix Bug":
        prompt = f"""
        Fix the following code.
        Return only corrected code.

        {user_input}
        """

    elif feature == "Explain Code":
        prompt = f"""
        Explain this code simply:

        {user_input}
        """

    elif feature == "Improve English":
        prompt = f"""
        Correct grammar and improve:

        {user_input}
        """

    elif feature == "Chat":
        prompt = user_input

    else:
        output_box.insert(tk.END, "Invalid option\n")
        return

    output_box.insert(tk.END, "\n⏳ Processing...\n")
    root.update()

    result = ask_ai(prompt)

    output_box.insert(tk.END, f"\n✅ Result:\n{result}\n")


# 🧹 Clear output
def clear_output():
    output_box.delete("1.0", tk.END)


# 🎨 GUI setup
root = tk.Tk()
root.title("🤖 AI Dev Assistant")
root.geometry("700x600")

# Dropdown
feature_var = tk.StringVar()
feature_dropdown = ttk.Combobox(root, textvariable=feature_var)
feature_dropdown["values"] = (
    "Generate Code",
    "Fix Bug",
    "Explain Code",
    "Improve English",
    "Chat"
)
feature_dropdown.current(0)
feature_dropdown.pack(pady=10)

# Input box
input_label = tk.Label(root, text="Enter your input:")
input_label.pack()

input_box = scrolledtext.ScrolledText(root, height=10)
input_box.pack(padx=10, pady=5, fill="both")

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

run_button = tk.Button(button_frame, text="Run", command=run_action)
run_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(button_frame, text="Clear", command=clear_output)
clear_button.pack(side=tk.LEFT, padx=5)

# Output box
output_label = tk.Label(root, text="Output:")
output_label.pack()

output_box = scrolledtext.ScrolledText(root, height=15)
output_box.pack(padx=10, pady=5, fill="both")

# Run app
root.mainloop()