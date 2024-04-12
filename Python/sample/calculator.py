import tkinter as tk

def on_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Calculator App")

entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Define buttons for numbers 1 to 9
for i in range(1, 10):
    row = (i - 1) // 3 + 1
    col = (i - 1) % 3
    button = tk.Button(root, text=str(i), padx=40, pady=20, command=lambda num=i: on_click(num))
    button.grid(row=row, column=col, padx=5, pady=5)

# Other buttons
button_0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda: on_click(0))
button_clear = tk.Button(root, text="C", padx=40, pady=20, command=clear)
button_equal = tk.Button(root, text="=", padx=40, pady=20, command=calculate)
button_add = tk.Button(root, text="+", padx=40, pady=20, command=lambda: on_click('+'))
button_subtract = tk.Button(root, text="-", padx=40, pady=20, command=lambda: on_click('-'))
button_multiply = tk.Button(root, text="*", padx=40, pady=20, command=lambda: on_click('*'))
button_divide = tk.Button(root, text="/", padx=40, pady=20, command=lambda: on_click('/'))

button_0.grid(row=4, column=0, padx=5, pady=5)
button_clear.grid(row=4, column=1, padx=5, pady=5)
button_equal.grid(row=4, column=2, padx=5, pady=5)
button_add.grid(row=1, column=3, padx=5, pady=5)
button_subtract.grid(row=2, column=3, padx=5, pady=5)
button_multiply.grid(row=3, column=3, padx=5, pady=5)
button_divide.grid(row=4, column=3, padx=5, pady=5)

root.mainloop()
