import os
import todoServices as ts


ToDos = ts.load()
def renderStart():
    print("Type H for help...")
    print("------------------")

def checkOperation(operation):
    if operation=="A":
        newToDo=input("Todo: ")
        ToDos.append((newToDo, False)) 
          
def checkHop(operation):
    if operation =="H":
            print("A | Add todo")
            print("C | Check todo")
            print("D | Delete todo")
            print("X | Exit program")
            
def render():
    
    print(".: Todo Manager :.")
    print("------------------")
    if len(ToDos)>0:        
        for i in ToDos:
            print(f"{ToDos.index(i)} [{"X" if i[1] else " "}] {i[0]} ")
    print("------------------")

if __name__ == "__main__":
   ts.clear()
   render()
   renderStart()
   while True:

    operation=input(">") 
    ts.operationChecker(operation, ToDos)
    ts.clear()
    # checkOperation(operation)
    render() 
    checkHop(operation)