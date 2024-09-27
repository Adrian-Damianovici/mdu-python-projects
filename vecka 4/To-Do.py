import os
import todoServices as ts


ToDos = ts.load()
def renderStart():
    print("Type H for help...")
    print("------------------")
            

if __name__ == "__main__":
   ts.clear()
   ts.render(ToDos)
   renderStart()
   while True:

    operation=input(">") 
    ts.operationChecker(operation, ToDos)
    ts.clear()
    ts.render(ToDos) 
