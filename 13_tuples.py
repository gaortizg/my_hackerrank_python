#############################################
# Define functions required for the program
#############################################
def get_valid_int(prompt: str) -> int:
    """
    Prompts the user for a positive integer input (1 <= n) and validates it.
    The function will continue to prompt the user until a valid input is received.

    Args:
        prompt (str): The message displayed to the user when asking for input.

    Returns:
        int: A valid positive integer input from the user.
    """
    while True:
        try:
            value = int(input(prompt).strip())
            if value > 0:
                return value
        except ValueError:
            pass
        
        print("Invalid input. Please enter a positive integer.")

#############################################
# Run the main program
#############################################
if __name__ == "__main__":
    n = get_valid_int("Enter the number of integers to accept: ")

    # Validate the tuple contains 'n' elements
    while True:
        try:
            values = tuple(map(int, input("Enter the values (space-separated): ").strip().split()))
            if len(values) == n:
                break
        except ValueError:
            pass
        print(f"Invalid input. Please enter exactly {n} integers.")
    
    # Compute the hash of the tuple and print result
    print(f"The hash of the tuple {values} is: {hash(values)}")