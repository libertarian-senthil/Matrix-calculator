#  Status: active
"""
This is the CLI(Command Line Interface) for matrix calculator.
"""

from numpy import string_
from matrix import arithmetic, formula

while True:
    """ Loop terminates only if there's no invalid input """

    print("""\
        ********************Matrix Calculator******************
            1. Addition
            2. Subtraction
            3. Multiplication
            4. Square of matrix 
            5. Transpose of matrix
            6. Exit
        """)
    try:
        option= int(input("Enter an option: "))
    except ValueError:
        print("Invalid input Enter the option between 1 and 6: ")
    else:
         break

# Creating objects for arithmetic and formula classes
oper_arithmetic = arithmetic.arithmetic()
operation_for = formula.formula()

def Type_cast(data):
    """
    Convert the given data type into integer. for use by dimension in other matrix operations.

    Parameters
    ----------
    data : String
        Used for typecasting.
    
    Returns
    -------
        Return integer value. 
    """
    
    try:
        Int = int(data)
    except ValueError:
        return "Invalid dimension Enter a integer"
    else:
        return Int

# Processing the input from the option.
if option == 1:     # Addition
    print("addition") 
    ip = input("Enter the No. of dimensions:")
    if ip == "quit": 
        print("Exited")
    else:
        val = Type_cast(ip)
        if type(val) == int:
            print(oper_arithmetic.add(val))
            input("Press Enter key to exit... ")
        else:
            print("Invalid input: Exited")

elif option == 2:   # Subtraction
    print("Subtraction") 
    ip= input("Enter the No. of dimensions:")
    if ip == "quit":
        print("Exited")
    else:
        val = Type_cast(ip)
        if type(val) == int:
            print(oper_arithmetic.sub(val))
            input("Press Enter key to exit... ")
        else:
            print("Invalid input: Exited")

elif option == 3:   # Multiplication
    print("Multiplication") 
    ip= input("Enter the No. of dimensions:")
    if ip == "quit":
        print("Exited")
    else:
        val = Type_cast(ip)
        if type(val) == int:
            print(oper_arithmetic.multi(val))
            input("Press Enter key to exit... ")
        else:
            print("Invalid input: Exited")

elif option == 4:   # Squaring
    print("square of A") 
    ip= input("Enter the No. of dimensions:")
    if ip == "quit":
        print("Exited")
    else:
        val = Type_cast(ip)
        if type(val) == int:
            print(operation_for.square(val))
            input("Press Enter key to exit... ")
        else:
            print("Invalid input: Exited")

elif option == 5:   # Transpose
    print("transpose")   
    ip= input("Enter the No. of dimensions:")
    if ip == "quit":
        print("Exited")
    else:
        val = Type_cast(ip)
        if type(val) == int:
            print(operation_for.trans(val))
            input("Press Enter key to exit... ")
        else:
            print("Invalid input: Exited")

elif option == 6:   # Quit
    print("Exited") 

else: 
    print("Invalid input") 