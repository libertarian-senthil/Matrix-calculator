# Status: active

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Matrix calculator")
root.geometry("950x650")
root.resizable(False, False)
root.columnconfigure(0, weight= 1)
root.columnconfigure(1, weight= 1)
root.columnconfigure(2, weight= 1)


operations = ttk.Frame(root, border=3, relief=tk.SUNKEN)
operations.grid(row= 0, column=0)

part1= ttk.Frame(root, border=3, relief=tk.SUNKEN)
part1.grid(row=0, column=1)

l2= tk.Label(part1, text="A")
l2.grid(row= 0, column= 0, padx= 2, pady= 2)

l1= tk.Label(operations, text="A")
l1.grid(row= 0, column= 0, padx= 2, pady= 2)

root.mainloop()