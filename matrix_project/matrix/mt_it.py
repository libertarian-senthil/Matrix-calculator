#Basic matrix input file for all arithmetic values
def empt(ch):
    ''' matrix addition'''
    while True:
        a = [[0,0], 
            [0,0]
            ]
        try:
            for i in range(2):
                for j in range(2):
                    e = int(input(f"{ch}:"))
                    a[i][j] = e
            return a
        except ValueError:
            print("You've given a incorrect input")
if __name__ == '__main__':
    print(empt('a'))
