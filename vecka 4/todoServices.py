import os
import json

def save(list):
    with open("savefile.json", mode="w+") as saveFile:
     json.dump(list, saveFile)

def load():
    with open("savefile.json", mode="r") as saveFile:
        return json.load(saveFile)

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
            helpOperation()
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
    index = int(input("Index: "))
    list.pop(index)
def checkOperation(list):
    index = int(input("index: "))
    list[index][1] = True

def exitProgramOperation(list):
    save(list)
    print("TODOS Saved Successfuly...")
    exit()

def helpOperation():
    print("A | Add todo")
    print("C | Check todo")
    print("D | Delete todo")
    print("X | Exit program")