#  Status: active
"""
This is the CLI(Command Line Interface) for matrix calculator.
"""

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
        option= eval(input("Enter an option: "))
    except NameError:
        print("Invalid input")
    else:
         break

# Creating objects for arithmetic and formula classes
oper_arithmetic = arithmetic.arithmetic()
operation_for = formula.formula()

# Processing the input from the option.
if option == 1:     # Addition
    print("addition") 
    ip= input("Enter the No. of dimensions:")
    if ip == "quit":
        print("Exited")
    else:
        print(oper_arithmetic.add(eval(ip)))
        input("Press Enter key to exit... ")
elif option == 2:   # Subtraction
    print("Subtraction") 
    ip= input("Enter the No. of dimensions:")
    if ip == "quit":
        print("Exited")
    else:
        print(oper_arithmetic.sub(eval(ip)))
        input("Press Enter key to exit... ")
elif option == 3:   # Multiplication
    print("Multiplication") 
    ip= input("Enter the No. of dimensions:")
    if ip == "quit":
        print("Exited")
    else:
        print(oper_arithmetic.multi(eval(ip)))
        input("Press Enter key to exit... ")
elif option == 4:   # Squaring
    print("square of A") 
    ip= input("Enter the No. of dimensions:")
    if ip == "quit":
        print("Exited")
    else:
        print(operation_for.square(eval(ip)))
        input("Press Enter key to exit... ")
elif option == 5:   # Transpose
    print("transpose")   
    ip= input("Enter the No. of dimensions:")
    if ip == "quit":
        print("Exited")
    else:
        print(operation_for.trans(eval(ip)))
        input("Press Enter key to exit... ")
elif option == 6:   # Quit
    print("Exited") 
else: 
    print("Invalid input") 