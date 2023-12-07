import tkinter as tk
from math import sqrt

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        # Entry widget to display input and results
        self.entry = tk.Entry(root, width=20, font=('Arial', 16), justify='right')
        self.entry.grid(row=0, column=0, columnspan=5, pady=5)

        # Buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '+', '='
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(root, text=button, width=5, height=2, command=lambda b=button: self.on_button_click(b)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Additional buttons
        tk.Button(root, text='C', width=5, height=2, command=self.clear_entry).grid(row=5, column=0, columnspan=2)
        tk.Button(root, text='⌫', width=5, height=2, command=self.backspace).grid(row=5, column=1, columnspan=2)
        tk.Button(root, text='√', width=5, height=2, command=self.square_root).grid(row=5, column=3)

        # Memory variable
        self.memory = 0

    def on_button_click(self, button):
        current_text = self.entry.get()

        if button == '=':
            try:
                result = eval(current_text)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")

        elif button == 'C':
            self.clear_entry()

        elif button == '⌫':
            self.backspace()

        elif button == '√':
            try:
                result = sqrt(float(current_text))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")

        else:
            self.entry.insert(tk.END, button)

    def clear_entry(self):
        self.entry.delete(0, tk.END)

    def backspace(self):
        current_text = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, current_text[:-1])

    def square_root(self):
        try:
            result = sqrt(float(self.entry.get()))
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
