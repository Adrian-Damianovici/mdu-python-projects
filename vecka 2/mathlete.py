cardinality = 0 #amount of inputs
total = 0

print(".: MATHLETE :.")
print("--------------")

while True:
    userInput = input(">")
    if userInput == "exit":
        break
    try:
        float(userInput)
            
    except:
        print("ERROR: invalid number!")
    else:                                   #runs on success
        cardinality += 1
        total += float(userInput)


print("--------------")
print("Cardinality: " + str(cardinality))
print("Sum: " + str(total))
try:
    str(total/cardinality)
except ZeroDivisionError:
    print("mean: " + "Undefined")
else:
    print("mean: " + str(total/cardinality))


