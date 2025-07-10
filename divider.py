def divide_first_last(numbers):
    """
    Returns the integer division result of the first and last number in the list.
    Raises an exception if the last number is zero.
    """
    print(f"List before division: {numbers}")
    if numbers[-1] == 0:
        raise ZeroDivisionError("Cannot divide by zero (last number is zero).")
    result = numbers[0] // numbers[-1]
    print(f"Division result of first and last number: {result}")
    return numbers
