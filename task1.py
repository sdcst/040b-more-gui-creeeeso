import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("tk")

label1 = tk.Label(window,text="Principal")
label2 = tk.Label(window,text="Interest Rate")
label3 = tk.Label(window,text="Years")
label4 = tk.Label(window,text="Amount")
label5 = tk.Label(window,text="-")
entry1 = tk.Entry(window, width=15)
entry2 = tk.Entry(window, width=15)
combobox3 = ttk.Combobox(window, width = 15)
entry4 = tk.Entry(window, width=15)

label1.grid(row=1,column=1)
label2.grid(row=1,column=2)
label3.grid(row=1,column=3)
entry1.grid(row=2,column=1)
entry2.grid(row=2,column=2)
combobox3.grid(row=2,column=3)
label5.grid(row=3,column=1)
label4.grid(row=4,column=1,sticky=E)
entry4.grid(row=4,column=2)

window.mainloop()