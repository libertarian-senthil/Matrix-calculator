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
    Convert the given data(also iterable object) type into integer. for use by dimension in other matrix operations.

    Parameters
    ----------
    data : String
        Used for typecasting.
    
    Returns
    -------
        Return integer value. 
    """
    if type(data) == str:
        try:
            Int = int(data)
        except ValueError:
            return None
        else:
            return Int
    if type(data) == list:
        try: 
            return [int(data[i]) for i in range(len(data))]
        except ValueError:
            return None 

def isNone(data:list):
    """"
    Find whether the given iterable object(list) contains any None data type and return True if found None data type.

    Parameters
    ----------
    data : list
        used to find the None data type
    Returns
    -------
        True if found None else False
    """
    
    for i in range(len(data)):
        if data[i]  == None:
            fact = True
    return fact


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
    print("""Multiplication:
>Enter the dimensions like 2x3 or enter 'quit' to exit the program.
>Remember column of first matrix must be equal to the row of second matrix
>Any unwanted inputs might lead to the program termination or inappropriate output
""")
    try:
        ip1= input("Enter dimension for first matrix: ").lower()       # getting and converting input to lower case
        if ip1 == "quit":
            print("Exited")
        ip2= input("Enter dimension for second matrix: ").lower()      # getting and converting input to lower case
        if ip2 == "quit":
            print("Exited")
        
        if len(ip1) == 3 and len(ip2) == 3:
            if ip1[1] == "x":       # checking for proper dimension
                ip1 = ip1.split("x")
            else:
                print("invalid dimension: exited")
            if ip2[1] == "x":       # checking for proper dimension
                ip2 = ip2.split("x")
            else:
                print("invalid dimension: exited")
            # print(ip1[0], ip1[1], ip2[0], ip2[1], sep= " ") #test
            ip1, ip2 = Type_cast(ip1), Type_cast(ip2)
            if (None not in ip1) and (None not in ip2):
                if ip1[1] == ip2[0] :
                    print(oper_arithmetic.multi(ip1[0], ip1[1], ip2[0], ip2[1]))
                else:
                    print("mismatch of column of first and row of second  matrix\n process stopped: exited")
            else:
                print("Incorrect dimension\n process stopped and exited")
        else:
            print("incorrect dimension\n process stopped and exited")
    except:
        print("Error occurred due to unintended input \n process stopped and exited")
    finally:
        input("Press enter to exit...")
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