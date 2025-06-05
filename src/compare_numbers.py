# 1. Pide al usuario dos números. Imprime cuál de los dos números es mayor. Si son iguales, imprímelo.
# 1. Ask the user for numbers. Print which number of numbers is larger. If they are the same, print it.

def get_number(prompt: str):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            raise ValueError("Please insert a valid number")
    
def compare_two_numbers(number_1: float, number_2:float):
        if number_1 == number_2:
            return f"The numbers are equal: {number_1}"
        else:
            bigger_number = max(number_1, number_2)
            smaller_number = min(number_1, number_2)
            return f"{bigger_number} is bigger than {smaller_number}"

if __name__ == "__main__": # pragma: no cover
    number_1 = get_number("Insert first number: ")
    number_2 = get_number("Insert second number: ")
    print(compare_two_numbers(number_1, number_2))
