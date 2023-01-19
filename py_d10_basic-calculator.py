print(
    '''
 _____________________   
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
    '''
)
status = True
progress = 'n'

def add(first, second):
    calc = first + second
    return calc


def sub(first, second):
    calc = first - second
    return calc


def mul(first, second):
    calc = first * second
    return calc


def dvd(first, second):
    calc = first / second
    return calc

while status == True:

    if progress == 'n':
        first_num = int(input("Enter first no: "))
    operator = ['+','-',"*","/"]
    print(operator)
    operator_input = input("Select the operator: ")
    second_num = int(input("Enter second no: "))

    if operator_input == '+':
        result = add(first_num,second_num)
    elif operator_input == '-':
        result = sub(first_num,second_num)
    elif operator_input == '*':
        result = mul(first_num,second_num)
    elif operator_input == '/':
        result = dvd(first_num,second_num)
    else:
        print("Invalid Input.")

    print(result)
    progress = input('''Type 'y' if you want to continue calculation with current result. 
Type 'n' to start a new calculation.
Type 'exit' to stop calculation: ''').lower()

    if progress == 'y':
        first_num = result
    elif progress == 'exit':
        status = False


