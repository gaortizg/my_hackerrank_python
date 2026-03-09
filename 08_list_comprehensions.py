def get_valid_int(prompt: str) -> int:
    """
    Prompts the user for a positive integer input and validates it. The function will continue to prompt the user until a valid input is received.

    Args:
        prompt (str): The message displayed to the user when asking for input.

    Returns:
        int: A valid positive integer input from the user.
    """
    while True:
        try:
            value = int(input(prompt).strip())
            if value <= 0:
                print("Invalid input. Please enter a positive integer greater than zero.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter an integer only.")


if __name__ == "__main__":
    x = get_valid_int("Enter a positive integer for x: ")
    y = get_valid_int("Enter a positive integer for y: ")
    z = get_valid_int("Enter a positive integer for z: ")
    n = get_valid_int("Enter a positive integer for n: ")
    
    # Perform all possible permutations and print valid results only
    valid_perms = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n]
    print(valid_perms)