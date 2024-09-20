import os

ToDos=[]

print(".: Todo Manager :.")
print("------------------")
if len(ToDos)>0:        
        for i in range(len(ToDos)):
            print( ToDos[i])
print("------------------")
print("Type H for help...")
print("------------------")

def checkOperation(operation):
    if operation=="A":
        newToDo=input("Todo: ")
        ToDos.append(newToDo) 
          
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
        for i in range(len(ToDos)):
            print( ToDos[i])
    print("------------------")

if __name__ == "__main__":
   while True:

    operation=input(">") 
    os.system("cls")
    checkOperation(operation)
    render() 
    checkHop(operation)