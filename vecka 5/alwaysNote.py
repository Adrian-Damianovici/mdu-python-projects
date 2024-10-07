import json
import os

def load():
    try:
        with open("save.json", mode="r") as saveFile:
            file = saveFile.read()
            if type(file) == None:
                with open("save.json", mode="w") as saveFile:
                    json.dump({}, saveFile)
                return load()
            else:
                return json.loads(file)

    except FileNotFoundError:
        with open("save.json", mode="w") as saveFile:
            json.dump({}, saveFile)
        return load()
        

def save(data):
    with open("save.json", mode="w") as saveFile:
        json.dump(data, saveFile)

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")



def addNote(data):
    name = input("note > ")
    text = input("text > ")
    data.update({name: text}) 

def viewNote(data):
    name = input("note > ")
    try:
        print("-"*18)
        print(data[name])
        print("-"*18)
        input("press ENTER to continue...")
    except KeyError:
        print("ERROR: note not found!")
        print("-"*18)
        input("pres ENTER to continue...")
        

def delNote(data):
    name = input("Note >")
    try:
        del data[name]
    except KeyError:
        print("-"*18)
        print("ERROR: note not found!")
        print("-"*18)
        input("pres ENTER to continue...")

def exitNote(data):
    save(data)
    print("INFO: data saved successfuly!")
    exit()

def renderNotes(data):
    for i in data:
        print(f"- {i}")

def header(data):
    print(".:  ALWAYSNOTE  :.")
    print("-- Gold Edition --")
    print("*"*18)
    renderNotes(data)
    print("-"*18)
    print("view | view note")
    print("add  | add note")
    print("rm   | delete note")
    print("exit | exit program")
    print("-"*18)




def main():
    data = load()
    while True:
        clear()
        header(data)
        operation = input("menu > ")
        match operation:
            case "view":
                viewNote(data)
            case "add":
                addNote(data)
            case "rm":
                delNote(data)
            case "exit":
                exitNote(data)
            case _:
                print("-"*18)
                print("ERROR: Invalid operation")
                print("-"*18)
                input("press ENTER to continue...")

            

if __name__ == "__main__":
    main()