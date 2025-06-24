import tkinter as tk
import string

def check_strength():
    pwd = password_entry.get()
    length = len(pwd)

    has_upper = any(c.isupper() for c in pwd)
    has_lower = any(c.islower() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    has_symbol = any(c in string.punctuation for c in pwd)

    score = sum([has_upper, has_lower, has_digit, has_symbol])

    if length < 6:
        strength = "Too short — Weak"
        color = "red"
    elif score == 4 and length >= 10:
        strength = "Strong 💪"
        color = "green"
    elif score >= 3:
        strength = "Moderate"
        color = "orange"
    else:
        strength = "Weak"
        color = "red"

    result_label.config(text=strength, fg=color)

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x250")
root.configure(bg="#F0F8FF")  # Alice Blue

font_style = ("Arial", 12)

tk.Label(root, text="Enter your password:", font=font_style, bg="#F0F8FF").pack(pady=15)
password_entry = tk.Entry(root, font=font_style, show="*", width=30, bg="#FFF5EE")
password_entry.pack()

tk.Button(root, text="Check Strength", font=font_style,
          command=check_strength, bg="#FF7F50", fg="white").pack(pady=15)

result_label = tk.Label(root, text="", font=("Arial", 14), bg="#F0F8FF")
result_label.pack(pady=10)

root.mainloop()
