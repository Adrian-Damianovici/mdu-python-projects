import os

def clear():
    os.system("cls")

def formatNotation(number):
    if len(str(number)) > 12:
        return "{:e}".format(number)
    else:
        return number

def multiply(a, b):
    result = a * b
    
    return formatNotation(result)
def division(a, b):
    try:
       a/b
    except ZeroDivisionError:
        return "infinity"
    else:
        return formatNotation(a/b)
def addition(a, b):
    return formatNotation(a + b)
def subtraction(a, b):
    return formatNotation(a-b)

def floatValidator(numb):
    var = input(f"{numb}= ")
    try:
        float(var)
    except ValueError:
        print("----------------------------")
        print(f"invalid float({var})")
        print("----------------------------")
        return floatValidator(numb)
    else: 
        return float(var)
    
def selectOperation(userInput, a, b):
    '''Selects which operation should be used based on input'''
    match userInput:
        case "add":
           return addition(a, b)
        case "sub":
           return subtraction(a, b)
        case "mul":
            return multiply(a, b)
        case "div":
           return division(a, b)
        case _:
            print("Invalid operation")
            
def numberTypeCheck(number: str):
    if number.is_integer():
        return int(number)
    else:
        return number

def FormatExpression(a, b, operation, result):
    sign = ""
    match operation:
        case "add":
            sign = "+"
        case "sub":
            sign = "-"
        case "mul":
            sign = "*"
        case "div":
            sign = "/"
    return str(a) + sign + str(b) + "=" + str(result)