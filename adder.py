import random

def add_numbers(numbers):
    """Return and print the sum of numbers in the list."""
    total = 0
    for num in numbers:
        total += num
    print(f"Current sum of list: {total}")
    return total

def process_sum(numbers):
    """Make the sum even by appending random numbers (max 3 times)."""
    total = add_numbers(numbers)
    attempts = 0

    while total % 2 != 0 and attempts < 3:
        random_number = random.randint(0, 9)
        print(f"Sum is odd. Adding random number: {random_number}")
        numbers.append(random_number)
        print(f"List after adding: {numbers}")
        total = add_numbers(numbers)
        attempts += 1

    if total % 2 == 0:
        print("Sum is now even. Moving to multiplication step.")
    else:
        print("Sum is still odd after 3 tries. Moving to multiplication step anyway.")
    return numbers
