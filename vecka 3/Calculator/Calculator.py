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

def addHistory(item):
    if len(history) >= 3:
        history.pop(0)
    history.append(item)
    

def drawHistory(list):
    if len(list) > 0:
        for i in list:
            print(i)
    if len(list) < 3:
        for i in range(3-len(list)):
            print("\n", end="")


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
        


def numberTypeCheck(number):
    if number != 0 and type(number) == int or type(number) == float:
        if len(str(number).split(".")[1]) == 1 and str(number).split(".")[1] == "0":
            return(int(number))
        else:
            return(float(number))
    else:
        return(int(number))





def menuRender(history):
    '''Renders all of the interface'''
    print("----------------------------")
    print(f"{' ':<6} The Calculator {'':>6}")
    print("----------------------------")
    drawHistory(history)
    print("----------------------------")
    print("add | Add two numbers")
    print("sub | Subtract two numbers")
    print("mul | Multiply two numbers")
    print("div | Divide two numbers")
    print("----------------------------")

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

# TODO: Cleana upp koden
# TODO: Fixa så att koden pausas när man mattar in fel operation och ger användaren möjligheten att trycka
#       på enter för att fortsätta
# FIXME: Catch ValueError when inputing falsy float, ex. "7,3" or "banana"



def main():
    history = []
    while True:
        
        menuRender(history)
        operation = input(">")
        a = numberTypeCheck(float(input("a= ")))
        b = numberTypeCheck(float(input("b= ")))
        result = selectOperation(operation, a, b)
        if result != "infinity":
            result = numberTypeCheck(float(result))

        addHistory(FormatExpression(a, b, operation, result))
        clear()



if __name__ == "__main__":
    main()


