from adder import process_sum
from multiplier import process_product
from divider import divide_first_last

def get_integer_list():
    """Takes at least two integers as input from the user and returns them as a list."""
    while True:
        try:
            numbers = list(map(int, input("Enter at least two integers separated by space: ").split()))
            if len(numbers) < 2:
                raise ValueError("Please enter at least two integers.")
            return numbers
        except ValueError as e:
            print("Invalid input:", e)

if __name__ == "__main__":
    numbers = get_integer_list()

    numbers = process_sum(numbers)
    numbers = process_product(numbers)

    try:
        result = divide_first_last(numbers)
        print(f"Final Result (First element / Last element): {result}")
    except ZeroDivisionError as e:
        print("Error:", e)
