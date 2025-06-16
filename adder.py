import random

def add_numbers(numbers):
    """Returns the sum of all numbers in the list and prints it."""
    total = sum(numbers)
    print(f"Sum of list: {total}")
    return total

def process_sum(numbers):
    """
    Appends a random number (0-9) at most 3 times if sum is odd,
    until the sum becomes even. Returns the modified list.
    """
    append_count = 0
    total = add_numbers(numbers)

    while total % 2 != 0 and append_count < 3:
        rand_num = random.randint(0, 9)
        print(f"Sum is odd. Appending random number: {rand_num}")
        numbers.append(rand_num)
        print(f"List after appending: {numbers}")
        total = add_numbers(numbers)
        append_count += 1

    if total % 2 == 0:
        print("Sum is even. Proceeding to multiplication step.\n")
    else:
        print("Sum remained odd after 3 attempts. Proceeding anyway.\n")

    print(f"Final list after sum step: {numbers}\n")
    return numbers
