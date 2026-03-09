#############################################
# Define functions required for the program
#############################################
def split_and_join(s: str) -> str:
    """
    This function takes a string as input and returns a new string where each letter
    is separated by a hyphen.

    Parameters:
    s (str): The input string.

    Returns:
    str: The string with letters separated by hyphens.
    """
    return "-".join(s.split())

#############################################
# Run the main program
#############################################
if __name__ == "__main__":
    s = input("Enter a string: ")
    # Print the result of split_and_join function
    print(split_and_join(s))