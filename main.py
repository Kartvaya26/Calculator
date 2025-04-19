import tkinter as tk


root = tk.Tk()
root.title("Calculator")
root.geometry("400x400")


display = tk.Entry(root, font=("Arial", 20), borderwidth=2, relief="ridge", justify="right")
display.pack(padx=10, pady=10, fill="x")


def on_button_click(symbol):
    current = display.get()
    
    if symbol == "=":
        try:
            result = str(eval(current))
            display.delete(0, tk.END)
            display.insert(0, result)
        except:
            display.delete(0, tk.END)
            display.insert(0, "Error")
    
    elif symbol == "C":
        display.delete(0, tk.END)
    
    else:
        display.insert(tk.END, symbol)


btn_frame = tk.Frame(root)
btn_frame.pack()


buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]


for row_index, row in enumerate(buttons):
    for col_index, symbol in enumerate(row):
        button = tk.Button(
            btn_frame,
            text=symbol,
            font=("Arial", 18),
            width=5,
            height=2,
            command=lambda s=symbol: on_button_click(s)  
        )
        button.grid(row=row_index, column=col_index, padx=5, pady=5)


root.mainloop()
