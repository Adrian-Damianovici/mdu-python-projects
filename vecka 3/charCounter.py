

def char_counter(text, letter):
    matches = 0
    i = 0
    while i < len(text):
        if text[i].lower() == letter.lower():
            matches +=1
        i+=1
    return matches

sentence = input("Ange en text! ")
letter = input("ange en bokstav! ")

print(f'there are {char_counter(sentence, letter)} "{letter}"s in {sentence}!')


