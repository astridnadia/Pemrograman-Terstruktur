# Function 
def starPattern(n):
    space = 2*n - 1
    for i in range(n):
        print(('*'*(2*i+1)).center(space))
def starPattern2(n):
    space = 1+ 2*n
    for i in range(n):
        print(('*'*(5-2*i)).center(space))
starPattern(4)
starPattern2(3)


