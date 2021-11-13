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


if __name__ == "__main__":
    a= Type_cast("senthilnathan")
    b = Type_cast("1")

    if a == int:
        print(a)
    else:
        print("str")
    if b == int:
        print(b) 
    else:
        print("str")