#  Status: active
# Creating a cmd line interface for application.
#  This module gets options for the matrix calculation and finally displays the result.


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

# Processing the input to the option.
# We can give the No. of dimension needed in non-programming side
oper_arithmetic = arithmetic.arithmetic()
operation_for = formula.formula()
if option == 1:
    print("addition") #test code
    ip= input("Enter the No. of dimensions:")
    if ip == "quit":
        print("Exited")
    else:
        print(oper_arithmetic.add(eval(ip)))
        input("Press Enter key to exit... ")
elif option ==2:
    print("Subtraction") #test code
    ip= input("Enter the No. of dimensions:")
    if ip == "quit":
        print("Exited")
    else:
        print(oper_arithmetic.sub(eval(ip)))
        input("Press Enter key to exit... ")
elif option == 3:
    print("Multiplication") #test code
    ip= input("Enter the No. of dimensions:")
    if ip == "quit":
        print("Exited")
    else:
        print(oper_arithmetic.multi(eval(ip)))
        input("Press Enter key to exit... ")
elif option == 4:
    print("square of A") #test code
    ip= input("Enter the No. of dimensions:")
    if ip == "quit":
        print("Exited")
    else:
        print(operation_for.square(eval(ip)))
        input("Press Enter key to exit... ")
elif option == 5:
    print("transpose")   # test code
    ip= input("Enter the No. of dimensions:")
    if ip == "quit":
        print("Exited")
    else:
        print(operation_for.trans(eval(ip)))
        input("Press Enter key to exit... ")
elif option == 6:
    print("Exited") 
else: 
    print("Invalid input") 