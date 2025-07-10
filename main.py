from adder import process_sum
from multiplier import process_product
from divider import divide_first_last
from average import calculate_average


pipeline_steps = [
    ("summation", process_sum),
    ("multiplication", process_product),
    ("division", divide_first_last),
    ("averaging", calculate_average)
]

def get_integer_list():
    """Takes at least two integers as input from the user and returns them as a list."""
    while True:
        try:
            user_input = input("Enter at least two integers separated by space: ")
            numbers = [int(num) for num in user_input.split()]

            if len(numbers) < 2:
                raise ValueError("You must enter at least two integers.")
            return numbers
        except ValueError as e:
            print(f"Invalid input: {e}\nPlease try again.\n")

if __name__ == "__main__":
    numbers = get_integer_list()
    print(f"Initial list: {numbers}")

    for step_name, step_function in pipeline_steps:
        print(f"\n starting {step_name} process...")
        numbers = step_function(numbers)
        print(f"\n List after {step_name} step: {numbers}")
    
    



