#############################################
# Define functions required for the program
#############################################
def wrap(string: str, max_width: int) -> str:
    """
    Wraps the input string into lines of specified maximum width.

    Parameters:
    string (str): The input string to be wrapped.
    max_width (int): The maximum width of each line.

    Returns:
    str: The wrapped string with lines separated by newline characters.
    """
    wrapped_string = ""
    for i in range(0, len(string), max_width):
        wrapped_string += string[i:i+max_width] + "\n"
    return wrapped_string.strip()  # Remove the trailing newline



#############################################
# Run the main program
#############################################
if __name__ == "__main__":
    # Validate string is not empty
    while not (string := input("Enter a string: ")) or len(string) > 1000:
        print("String cannot be empty nor longer than 1000 characters.")

    # Validate max_width is a positive integer
    while True:
        try:
            max_width = int(input("Enter the maximum width: "))
            if max_width > 0 and max_width <= len(string):
                break
            else:
                print("Maximum width must be a positive integer not exceeding the string length.")
        except ValueError:
            print("Please enter a valid integer for maximum width.")

    # Wrap the string and print the result
    wrapped_string = wrap(string, max_width)
    print(wrapped_string)
