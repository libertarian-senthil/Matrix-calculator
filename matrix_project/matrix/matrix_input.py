# Creating a cmd line interface for application.
#  This module gets options for the matrix calculation and finally displays the result.

while True:
    """ Loop terminates only if there's no invalid input """

    print("""\
        ********************Matrix Calculator******************
            1. Addition
            2. Subtraction
            3. Multiplication
            4. Division
            5. Exit
        """)
    try:
        option= eval(input("Enter an option: "))
    except NameError:
        print("Invalid input")
    else:
         break

# Processing the input to the option.
if option == 1:
    print("addition") #test code
elif option ==2:
    print("Subtraction") #test code
elif option == 3:
    print("Multiplication") #test code
elif option == 4:
    print("Divsion") #test code
elif option == 5:
    print("Exited") 
else: 
    print("Invalid input") 