# """CLI application for a prefix-notation calculator."""

from arithmetic import add, subtract, multiply, divide, square, cube, power, mod
# input_string = 'pow 3 5'
# tokens = input_string.split(' ')   # => ['pow', '3', '5']


def function_name():
    try_again=input('enter q to quit, otherwise press enter to calculate>:')
    while try_again != "q":
        input_string=input("enter the function and numbers to use in the calculation, separated by the source:")
        tokens=input_string.split()

        if tokens[0]=='add':
            print(add(int(tokens[1]),int(tokens[2])))
        elif tokens[0]=='subtract':
            print(subtract(int(tokens[1]),int(tokens[2])))
        elif tokens[0]=='multiply':
            print(multiply(int(tokens[1]),int(tokens[2])))
        elif tokens[0]=='divide':
            print(divide(int(tokens[1]),int(tokens[2])))
        elif tokens[0]=='square':
            print(square(int(tokens[1])))
        elif tokens[0]=='cube':
            print(cube(int(tokens[1])))
        elif tokens[0]=='power':
            print(power(int(tokens[1]),int(tokens[2])))
        elif tokens[0]=='modulo':
            print(mod(int(tokens[1]),int(tokens[2])))
        
        if input_string == 'q':
            try_again = 'q'
 
function_name()