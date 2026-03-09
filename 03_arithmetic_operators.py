def get_valid_int(prompt: str) -> int:
    """
    Prompts the user for a positive integer input (0< n < 100) and validates it. The function will continue to prompt the user until a valid input is received.

    Args:
        prompt (str): The message displayed to the user when asking for input.

    Returns:
        int: A valid positive integer input from the user.
    """
    while True:
        try:
            n = int(input(prompt).strip())
            if n <= 0 or n > 10**10:
                print("Invalid input. Please enter integers between 1 and 10**10: ")
                continue
            return n
        except ValueError:
            print("Invalid input. Please enter integers between 1 and 10**10: ")

if __name__ == "__main__":
    # Validate input for 'a' and 'b' (0 < a,b < 10**10)
    a = get_valid_int("Enter integer a: ")
    b = get_valid_int("Enter integer b: ")

    # Perform arithmetic operations and print results
    print(f"a + b = {a + b}")
    print(f"a - b = {a - b}")

    print(f"a * b = {a * b}")
