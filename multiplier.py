import random
import math

def multiply_numbers(numbers):
    """Returns the product of all numbers in the list and prints it."""
    result = math.prod(numbers)
    print(f"Product of list: {result}")
    return result

def process_product(numbers):
    """
    Appends a random number (0-9) at most 3 times if product is odd,
    until the product becomes even. Returns the modified list.
    """
    append_count = 0
    product = multiply_numbers(numbers)

    while product % 2 != 0 and append_count < 3:
        rand_num = random.randint(0, 9)
        print(f"Product is odd. Appending random number: {rand_num}")
        numbers.append(rand_num)
        print(f"List after appending: {numbers}")
        product = multiply_numbers(numbers)
        append_count += 1

    if product % 2 == 0:
        print("Product is even. Proceeding to division step.\n")
    else:
        print("Product remained odd after 3 attempts. Proceeding anyway.\n")

    return numbers
