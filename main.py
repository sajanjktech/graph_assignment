from adder import process_sum
from multiplier import process_product
from divider import divide_first_last

def get_integer_list():
    """Takes at least two integers as input from the user and returns them as a list."""
    while True:
        try:
            user_input = input("Enter at least two integers separated by space: ")
            numbers = list(map(int, user_input.split()))
            
            if len(numbers) < 2:
                raise ValueError("You must enter at least two integers.")
            return numbers
        except ValueError as e:
            print(f"Invalid input: {e}\nPlease try again.\n")

if __name__ == "__main__":
    numbers = get_integer_list()
    print(f"Initial list: {numbers}")

    numbers = process_sum(numbers)
    print("Proceeding to product stage...\n")

    numbers = process_product(numbers)
    print("Proceeding to division stage...\n")

    try:
        result = divide_first_last(numbers)
        print(f"Final Result (First element / Last element): {result}")
    except ZeroDivisionError as e:
        print("Error:", e)
