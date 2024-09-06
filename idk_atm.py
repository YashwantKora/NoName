import tkinter as tk
from tkinter import ttk
from tkinter import messagebox #<--not in use


def temperature_window():
    temperature_window = tk.Toplevel()
    temperature_window.title('Extra Window')
    temperature_window.geometry('300x400')
   
    mainframe2 = tk.Frame(temperature_window, bg='black')
    mainframe2.pack(fill='both', expand=True)
    
    def f_to_c():
        fahrenheit = float(text_box1.get())
        celsius = (fahrenheit - 32) * 5/9
        result_label.config(text=f"{celsius:.2f}°C")

    def c_to_f():
        celsius = float(text_box2.get())
        fahrenheit = celsius * 9/5 + 32
        result_label.config(text=f"{fahrenheit:.2f}°C")
#F to C:
    label1 = ttk.Label(mainframe2, text="Enter a farhenheit value:", background='black', foreground='white', font=('poppins', 15))
    label1.grid(row=0, column=0)

    text_box1 = ttk.Entry(mainframe2)
    text_box1.grid(row=2, column=0, sticky='NWES', pady = 10)

    button3 = ttk.Button(mainframe2, text="Convert", command= f_to_c)
    button3.grid(row=3, column=0, sticky='NWES', pady = 10)
# C to F:                                           nice hack lol v
    label2 = ttk.Label(mainframe2, text="Enter a celsius value:      " ,background='black', foreground='white', font=('poppins', 15))
    label2.grid(row=4, column=0)

    text_box2 = ttk.Entry(mainframe2)
    text_box2.grid(row=5,column=0, sticky='NWES', pady=10)

    button4 = ttk.Button(mainframe2, text="Convert", command=c_to_f)
    button4.grid(row=6, column=0, sticky='NWES', pady=10) 

    result_label = ttk.Label(mainframe2, text="...", background='black', foreground='white', font=('poppins', 25) )
    result_label.grid(row=7, column=0, pady= 20, padx= 20) 
window = tk.Tk()
window.geometry('1000x600')
window.title("I have no idea what i am doing")

mainframe = tk.Frame(window, bg='black',)
mainframe.pack(fill='both', expand=True)


label = tk.Label(mainframe, text="Main Menu", foreground='white', background='black', font=('poppins', 30))
label.grid(row=0, column=1)

button1 = ttk.Button(mainframe, text="Temperature Converter", command=temperature_window)
button1.grid(row=1, column=0, pady=20, padx=40)

bt1_label = ttk.Label(mainframe, text="- Converts Fahrenheit to Celsius and vice versa!", background='black', foreground='white', font=('poppins', 15))
bt1_label.grid(row=1, column=1)

button2 = ttk.Button(mainframe, text="           To Do List           ")
button2.grid(row=2, column=0, pady = 20)

bt2_label = ttk.Label(mainframe, text="- To do list!", background='black', foreground='white', font=('poppins', 15))
bt2_label.grid(row=2, column=1)

window.mainloop()

