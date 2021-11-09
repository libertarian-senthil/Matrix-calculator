# Status: active

import tkinter as tk
from tkinter import ttk

# operations = ttk.Frame(root, border=3, relief=tk.SUNKEN)
# operations.grid(row= 0, column=0)

# part1= ttk.Frame(root, border=3, relief=tk.SUNKEN)
# part1.grid(row=0, column=1)

# l2= tk.Label(part1, text="A")
# l2.grid(row= 0, column= 0, padx= 2, pady= 2)

# l1= tk.Label(operations, text="A")
# l1.grid(row= 0, column= 0, padx= 2, pady= 2)


class Funtionality_area(ttk.Frame):
    """This class will be useful in creating functionality buttons in the leftmost side of the main window """

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        ttk.Label(self, text= "senthilnathan", width= 25,relief= "sunken").grid(row= 0, column= 0)  # Test code

class Middle_input(ttk.Frame):
    """This class will be useful in creating first matrix input templete on the midlle of the main window """

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
        ttk.Label(self, text= "ramchandran", width= 25,relief= "sunken").grid(row= 0, column= 0)    # Test code

class right_input(ttk.Frame):
    """This class will be useful in creating second matrix input templete on the midlle of the main window """

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
        ttk.Label(self, text= "deepika", width= 25,relief= "sunken").grid(row= 0, column= 0)    # Test code


class main_win(tk.Tk):
    """ This is the main window of the application """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Matrix calculator")
        self.geometry("950x650")
        # self.resizable(False, False)
        self.columnconfigure(0, weight= 1)
        self.columnconfigure(1, weight= 1)
        self.columnconfigure(2, weight= 1)        

        # Using the helloview widget
        Funtionality_area(self).grid(row= 0, column= 0, sticky= (tk.W + tk.E + tk.N + tk.S))
        Middle_input(self).grid(row= 0, column= 1, sticky= (tk.W + tk.E + tk.N + tk.S))
        right_input(self).grid(row= 0, column= 2, sticky= (tk.W + tk.E + tk.N + tk.S))


if __name__ ==  '__main__':
    main_window= main_win()
    main_window.mainloop()