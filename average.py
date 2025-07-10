import random
def calculate_average(numbers):
    """Prints the average of numbers in the list."""
    avg = sum(numbers) / len(numbers)
    print(f"Average of numbers: {round(avg)}")
    return round(avg)

def process_average(numbers):
    count = 0
    avg= calculate_average(numbers)

    while avg % 2 != 0 and count < 3:
        rand_num = random.randint(0, 9)
        print(f"Average is odd. Appending random number: {rand_num}")
        numbers.append(rand_num)
        print(f"List after appending: {numbers}")
        avg = calculate_average(numbers)
        count += 1
    if avg % 2 == 0:
        print("Average is even. Process completed successfully.\n") 
    else:
        print("Average remained odd after 3 attempts. Process completed anyway.\n")
    return numbers