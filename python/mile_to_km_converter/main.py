from tkinter import *


def convert_to_km():
    content = entry_box.get()
    conversion = float(content) * 1.60934
    conversion = int(conversion)
    km_label.config(text=conversion)


window = Tk()
window.title('Window to Km Converter')
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

entry_box = Entry(width=7)
entry_box.grid(column=1, row=1)

entry_label = Label(text='Miles')
entry_label.grid(column=2, row=1)

entry_label = Label(text='Km')
entry_label.grid(column=2, row=2)

equal_to_label = Label(text='is equal to')
equal_to_label.grid(column=0, row=2)

km_label = Label(text=0)
km_label.grid(column=1, row=2)

calculate_button = Button(text='Calculate', command=convert_to_km)
calculate_button.grid(column=1, row=3)

window.mainloop()
