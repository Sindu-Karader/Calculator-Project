# Python Tkinter Calculator
from tkinter import *
from tkinter.messagebox import showerror

# Functions
def add_text(text, strvar: StringVar):
    strvar.set(f'{strvar.get()}{text}')

def submit(entry: Entry, strvar: StringVar):
    operation = entry.get().replace("xx", "**")  # handle exponentiation with xx
    try:
        strvar.set(f"{strvar.get()}={eval(operation)}")
    except:
        showerror('Error!', 'Please enter a properly defined equation!')

# GUI
root = Tk()
root.title("PythonGeeks Calculator")
root.geometry('280x500')
root.resizable(0, 0)
root.configure(background='LightCyan2')

entry_strvar = StringVar(root)

Label(root, text='PythonGeeks Calculator', font=("Comic Sans MS", 15), bg='LightCyan2').place(x=25, y=0)
Label(root, text="Use 'xx' for exponentiation", font=("Georgia", 10), bg='LightCyan2').place(x=40, y=30)

eqn_entry = Entry(root, justify=RIGHT, textvariable=entry_strvar, width=22, font=12, state='normal')
eqn_entry.place(x=10, y=70)

# Buttons
buttons = [
    ('7', 5, 170), ('8', 65, 170), ('9', 125, 170), ('/', 195, 170),
    ('4', 5, 225), ('5', 65, 225), ('6', 125, 225), ('x', 195, 225),
    ('1', 5, 280), ('2', 65, 280), ('3', 125, 280), ('-', 195, 280),
    ('0', 5, 340), ('.', 65, 340), ('=', 125, 340), ('+', 195, 340),
    ('AC', 5, 110), ('(', 65, 110), (')', 125, 110), ('C', 195, 110)
]

for (text, x, y) in buttons:
    if text == '=':
        Button(root, height=2, width=5, text=text, font=9, bg='Blue',
               command=lambda e=eqn_entry, s=entry_strvar: submit(e, s)).place(x=x, y=y)
    elif text == 'AC':
        Button(root, height=2, width=5, text=text, font=9, bg='Red',
               command=lambda: entry_strvar.set('')).place(x=x, y=y)
    elif text == 'C':
        Button(root, height=2, width=5, text=text, font=9, bg='OrangeRed',
               command=lambda: entry_strvar.set(entry_strvar.get()[:-1])).place(x=x, y=y)
    elif text == 'x':
        Button(root, height=2, width=5, text=text, font=9, bg='DarkOrange',
               command=lambda: add_text('*', entry_strvar)).place(x=x, y=y)
    else:
        bg_color = 'Gold' if text.isdigit() else 'DarkOrange'
        Button(root, height=2, width=5, text=text, font=9, bg=bg_color,
               command=lambda t=text: add_text(t, entry_strvar)).place(x=x, y=y)

# Ok button
Button(root, height=2, width=22, text='Ok', font=9, bg='CadetBlue',
       command=lambda: root.destroy()).place(x=7, y=420)

root.mainloop()
