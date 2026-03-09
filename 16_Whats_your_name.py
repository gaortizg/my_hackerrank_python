#############################################
# Define functions required for the program
#############################################
def print_full_name(first: str, last: str) -> str:
    """
    This function takes a first name and last name as input and returns a new string
    with the full name.

    Parameters:
    first (str): The first name.
    last (str): The last name.

    Returns:
    str: A string using the full name.
    """
    return f"Hello {first} {last}! You just delved into python."

#############################################
# Run the main program
#############################################
if __name__ == "__main__":
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    # Print the result of print_full_name function
    print(print_full_name(first, last))