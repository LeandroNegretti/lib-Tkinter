import tkinter as tk

def press_btn(event):
    global expression
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(expression))
            display_var.set(result)
            expression = result
        except:
            display_var.set("Error")
            expression = ""
    elif text == "C":
        expression = ""
        display_var.set("")
    elif text == "Limpar":
        expression = expression[:-1]  
        display_var.set(expression)
    else :
        expression += text
        display_var.set(expression)

root = tk.Tk()
root.title("Calculadora")

expression = ""

display_var = tk.StringVar()

frame = tk.Frame(root)
frame.pack()

display = tk.Entry(frame, textvariable=display_var, font=("Arial", 18))
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+',
]

row = 1
col = 0

for btn_text in buttons:
    btn = tk.Button(frame, text=btn_text, font=("Arial", 14), width=5, height=2)
    btn.grid(row=row, column=col, padx=5, pady=5)
    btn.bind("<Button-1>", press_btn)
    col += 1
    if col > 3:
        col = 0
        row += 1

btn_clear = tk.Button(frame, text="Limpar", font=("Arial", 14), width=20, height=2)
btn_clear.grid(row=row, column=0, columnspan=4, padx=5, pady=5)
btn_clear.bind("<Button-1>", press_btn)

root.mainloop()