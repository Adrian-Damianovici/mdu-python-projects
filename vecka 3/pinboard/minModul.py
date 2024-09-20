import os
def clear():
    '''Rensar Skärmen'''
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def header(h1, h2, h3):
    '''Skirver ut anslagstavlan'''
    print(".: PINBOARD :.")
    print("--------------")
    print(f"- {h1}")
    print(f"- {h2}")
    print(f"- {h3}")
    print("--------------")