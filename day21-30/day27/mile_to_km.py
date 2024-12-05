from tkinter import *

FONT = ("Arial", 12)

def validate_input(value):
    return value == "" or value.replace(".", "", 1).isdigit()

def convert():
    if input_field.get() != "":
        miles = float(input_field.get())
        km = miles * 1.60934
        km_result_label.config(text=f"{km:.3f}")

window = Tk()
window.title("Miles to Kilometers")
window.minsize(width=250, height=150)
window.config(padx=20, pady=20)
for i in range(3):
    window.grid_rowconfigure(i, pad=10)
    window.grid_columnconfigure(i, pad=5)

validate_cmd = window.register(validate_input)

input_field = Entry(window, font=FONT, justify="center", validate="key", validatecommand=(validate_cmd, "%P"), width=10)
input_field.insert(END, "0")
input_field.grid(row=0, column=1)

miles_label = Label(window, text="miles", font=FONT)
miles_label.grid(row=0, column=2)

is_equal_label = Label(window, text="is equal to", font=FONT)
is_equal_label.grid(row=1, column=0)

km_result_label = Label(window, text="0", font=FONT)
km_result_label.grid(row=1, column=1)

km_label = Label(window, text="km", font=FONT)
km_label.grid(row=1, column=2)

convert_button = Button(window, text="Convert", font=FONT, command=convert)
convert_button.grid(row=2, column=1)

window.mainloop()
