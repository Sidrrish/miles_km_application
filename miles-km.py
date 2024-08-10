import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
# window.minsize(height=100, width=200)
window.config(padx=20, pady=20)


user_input = tkinter.Entry(width=10 )
user_input.grid(column=2, row=1)


def miles_km():
    c = float(user_input.get())
    ans.config(text=f"{int(c * 1.609344)}")


first_line = tkinter.Label(text="Miles")
first_line.grid(column=3, row=1)

second_line = tkinter.Label(text="is equal to")
second_line.grid(column=1, row=2)

ans = tkinter.Label(text=0)
ans.grid(column=2, row=2)

km = tkinter.Label(text="km")
km.grid(column=3, row=2)

calculate_button = tkinter.Button(text="Calculate", command=miles_km)
calculate_button.grid(column=2, row=3)


window.mainloop()
