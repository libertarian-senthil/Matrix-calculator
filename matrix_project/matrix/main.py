#  Status: active
# Creating a cmd line interface for application.
#  This module gets options for the matrix calculation and finally displays the result.

from arithmetic import * 

while True:
    """ Loop terminates only if there's no invalid input """

    print("""\
        ********************Matrix Calculator******************
            1. Addition
            2. Subtraction
            3. Multiplication
            4. Square of matrix 
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
    a= arithmetic()
    print(a.add(2))
elif option ==2:
    print("Subtraction") #test code
    b = arithmetic()
    print(b.sub(2))
elif option == 3:
    print("Multiplication") #test code
    c = arithmetic()
    print(c.multi(2))
elif option == 4:
    print("square of A") #test code
    d = arithmetic()
    print(d.square(2))
elif option == 5:
    print("Exited") 
else: 
    print("Invalid input") 