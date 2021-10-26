#Basic matrix input file for all arithmetic values
def matrix(ch):
    ''' matrix addition'''
    while True:
        a = [[0,0, 0], 
            [0,0, 0]
            ]
        try:
            for i in range(3):
                for j in range(3):
                    e = int(input(f"{ch}[{i}][{j}]: "))
                    a[i][j] = e
            return a
        except ValueError:
            print("You've given a incorrect input")
if __name__ == '__main__':
    print(matrix('a'))
