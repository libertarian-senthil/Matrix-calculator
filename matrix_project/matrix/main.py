#  Status: active
# Creating a cmd line interface for application.
#  This module gets options for the matrix calculation and finally displays the result.

from arithmetic import * 
from formula import *

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
if option == 1:
    print("addition") #test code
    a= arithmetic()
    print(a.add(eval(input("Enter the No. of dimensions:"))))
elif option ==2:
    print("Subtraction") #test code
    b = arithmetic()
    print(b.sub(eval(input("Enter the No. of dimensions:"))))
elif option == 3:
    print("Multiplication") #test code
    c = arithmetic()
    print(c.multi(eval(input("Enter the No. of dimensions:")))) #Need to change for multi dimensions like 2*3 and 3*2, Yet to be completed
elif option == 4:
    print("square of A") #test code
    d = formula()
    print(d.square(eval(input("Enter the No. of dimensions:"))))
elif option == 5:
    print("transpose")
    e = formula()
    print(e.transpose(eval(input("Enter the No. of dimensions:"))))
elif option == 6:
    print("Exited") 
else: 
    print("Invalid input") 