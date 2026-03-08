def get_valid_int(prompt: str) -> int:
    """
    Prompts the user for a positive integer input (<100) and validates it. The function will continue to prompt the user until a valid input is received.

    Args:
        prompt (str): The message displayed to the user when asking for input.

    Returns:
        int: A valid positive integer input from the user.
    """
    while True:
        try:
            n = int(input(prompt).strip())
            if n < 1 or n > 100:
                print("Invalid input. Please enter an integer between 1 and 100: ")
                continue
            return n
        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 100: ")

if __name__ == "__main__":
    n = get_valid_int("Enter integer between 1 and 100: ")
    
    # Check conditions of challenge and print result
    if (n % 2 == 1) or (n in range(6,21)):
        print("Weird")
    else:
        print("Not Weird")
