import tkinter as tk

def on_click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Erro")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Calculadora")
root.configure(bg='#F6BE00')

entry = tk.Entry(root, font=("Arial", 20), bd=5, relief=tk.SUNKEN, justify=tk.RIGHT)
entry.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", ".", "C", "+"),
]

for row in buttons:
    button_frame = tk.Frame(root)
    button_frame.pack(padx=10, pady=5)

    for text in row:
        button = tk.Button(button_frame, text=text, font=("Arial", 20), relief=tk.GROOVE, bd=3)
        button.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH, expand=True)
        button.bind("<Button-1>", on_click)

equal_button = tk.Button(root, text="=", font=("Arial", 20), relief=tk.GROOVE, bd=3)
equal_button.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
equal_button.bind("<Button-1>", on_click)

root.mainloop()
