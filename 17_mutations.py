#############################################
# Define functions required for the program
#############################################
def mutate_string(string: str, position: int, character: str) -> str:
    """
    This function takes a string, and changes the character at the specified position
    by the new character.

    Parameters:
    string (str): The input string.
    position (int): The position where the character will be changed.
    character (str): The new character to be placed at the specified position.

    Returns:
    str: The modified string.
    """
    return string[:position] + character + string[position+1:]

#############################################
# Run the main program
#############################################
if __name__ == "__main__":
    # Validate string is not empty
    while not (string := input("Enter a string: ")):
        print("String cannot be empty.")

    # Validate position is an integer and within the bounds of the string
    while True:
        try:
            position = int(input("Enter the position to change: "))
            if 0 <= position < len(string):
                break
            print("position must be within the bounds of the string.")
        except ValueError:
            print("Please enter a valid integer.")

    # Validate character is a single character
    while len(character := input("Enter the new character: ")) != 1:
        print("Please enter a single character.")

    # Print the mutated string
    print(mutate_string(string, position, character))