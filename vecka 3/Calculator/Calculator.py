import CalculatorServices as cs

def addHistory(item, history):
    '''
    simple function for adding a new element to the history and removing the oldest element 
    if the list lenght is larger than three elements
    '''
    if len(history) >= 3:
        history.pop(0)
    history.append(item)
    

def drawHistory(list):
    '''
    Function used for rendering the History section off the interface

    '''
    if len(list) > 0:
        for i in list:
            print(i)
    if len(list) < 3:
        for i in range(3-len(list)):
            print("\n", end="")
     

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

def main():
    cs.clear()
    while True:
        menuRender(history)
        operation = input(">")
        if operation not in ("add", "sub", "div", "mul"):
            print("----------------------------")
            print("Unknown Operation!")
            print("----------------------------")
            input("Press Enter to continue...")
            main()
            break
        
        a = cs.floatValidator("a")
        b = cs.floatValidator("b")

        a = cs.numberTypeCheck(a)
        b = cs.numberTypeCheck(b)


        result = cs.selectOperation(operation, a, b)
        if result != "infinity":
            result = cs.numberTypeCheck(float(result))

        addHistory(cs.FormatExpression(cs.formatNotation(a), cs.formatNotation(b), operation, cs.formatNotation(result)), history)
        cs.clear()

if __name__ == "__main__":
    history = []
    main()


