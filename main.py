import tkinter as tk

def on_button_click(name):
    pass

window = tk.Tk()
window.title("Tinh tien")



button_khang = tk.Button(window, text="Khang", command=lambda: on_button_click("khang"),padx=10,font=("Arial",12))
button_khang.grid(row=2,column=0)
entry_khang = tk.Entry(window)
entry_khang.grid()

button_duy = tk.Button(window, text="Duy", command=lambda: on_button_click("duy"),padx=20,font=("Arial",12))
button_duy.grid(row=2,column=2)
space_label = tk.Label(window, text="", padx=20)
space_label.grid(row=2,column=3)

button_huy= tk.Button(window, text="Huy", command=lambda: on_button_click("huy"),padx=20,font=("Arial",12))
button_huy.grid(row=2,column=4)
space_label = tk.Label(window, text="", padx=10)
space_label.grid(row=2,column=5)

button_den = tk.Button(window, text="Den", command=lambda: on_button_click("den"),padx=20,font=("Arial",12))
button_den.grid(row=2,column=6)
space_label = tk.Label(window, text="", padx=10)
space_label.grid(row=2,column=7)

window.geometry("500x400")
window.mainloop()


