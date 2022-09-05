# CALCULATOR PROJECT
#100 Days of Code, Dr. Angela Yu
#Student Łukasz Świątek Brzeziński

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(logo)


#Concatenation
def add (n1, n2):
    return n1 + n2

#Subtraction
def subtract (n1, n2):
    return n1 - n2

#Multiplication
def multiply (n1, n2):
    return n1 * n2

#Division
def divide (n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
    }


def calculator():
    num1 = float(input("What is the first number?: "))

    next_step = True

    while next_step:

        for key in operations:
            print(key)

        operation_symbol = input("Pick operation you want to make")
        num2 = float(input("What is the next number?: "))
        calculation = operations[operation_symbol]
        answer = calculation(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}") 
        if input("Do you want to add another operation (y, n)?".strip().lower()) == "y":
            next_step == True
            num1 = answer
        else:
            next_step = False
            calculator()

calculator()
            
