str1 = "katt"
str2 = "kanin"


index = 0
for char1, char2 in zip(str1, str2):
    if char1 != char2:
        break
    else:
        index +=1

print(index)




