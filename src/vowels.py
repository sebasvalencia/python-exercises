
def is_a_vowel(letter: str):
    if (letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u"):
        return True 
    else:
        return False

def print_is_a_vowel():
    letter = input("Insert a letter: ")
    if is_a_vowel(letter):
        print("Is a vowel")
    else:
        print("Is not a vowel")
 

if __name__ == "__main__": # pragma: no cover
    print_is_a_vowel()