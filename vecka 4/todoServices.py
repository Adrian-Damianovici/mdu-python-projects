import os
import json

showHelp = False

def save(list):
    with open("savefile.json", mode="w") as saveFile:
        json.dump(list, saveFile)

def load():
    try:
        with open("savefile.json", mode="r") as saveFile:
            file = saveFile.read()
            print(file)
            if type(file) == None:
                with open("savefile.json", mode="w") as saveFile:
                    json.dump([], saveFile)
                return load()
            else:
                return json.loads(file)

    except FileNotFoundError:
        with open("savefile.json", mode="w") as saveFile:
            json.dump([], saveFile)
        return load()


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def operationChecker(operation, list):
    match operation.lower():
        case "a":
            addOperation(list)
        case "c":
            checkOperation(list)
        case "d":
            deleteOperation(list)
        case "h":
            helpOperation(list)
        case "x":
            exitProgramOperation(list)
        case _:
            print("Unknown command")
            print("------------------")
            input("press ENTER to continue...")


def addOperation(list):
    newToDo=input("Todo: ")
    list.append([newToDo, False])

def deleteOperation(list):
    try:
        index = int(input("Index: "))
        list.pop(index)
    except (IndexError, ValueError):
        print("ERROR: Invalid index")
        print("------------------")
        input("Press ENTER to continue...")
def checkOperation(list):
    try: 
        index = int(input("index: "))
        list[index][1] = True
    except (IndexError, ValueError):
        print("ERROR: Invalid index")
        print("------------------")
        input("Press ENTER to continue...")
    

def exitProgramOperation(list):
    save(list)
    print("TODOS Saved Successfuly...")
    exit()

def helpOperation(list):
    global showHelp
    showHelp = True

def render(list):
    global showHelp
    print(".: Todo Manager :.")
    print("------------------")
    if len(list)>0:        
        for i in list:
            print(f"{list.index(i)} [{"X" if i[1] else " "}] {i[0]} ")
    else:
        print("Nothing to do!")
    print("------------------")
    if showHelp:
        print("A | Add todo")
        print("C | Check todo")
        print("D | Delete todo")
        print("X | Exit program")
        showHelp = False       