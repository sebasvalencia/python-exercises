
def even_or_odd(number: int) -> str:
    return "Even" if number % 2 == 0 else "Odd"

def print_is_even_or_odd():
    try:
        number = int(input("Insert a integer number: "))
        print(f"The number {number} is {even_or_odd(number)}")
    except ValueError:
        print("Invalid input. Please enter a integer.")

if __name__ == "__main__": #pragma: no cover
    print_is_even_or_odd()