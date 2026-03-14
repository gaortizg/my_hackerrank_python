#############################################
# Import the necessary modules and functions
#############################################
import string


#############################################
# Define functions required for the program
#############################################
def print_rangoli(size: int) -> None:
    """
    Print an alphabet rangoli of size N.
    Rangoli is a form of Indian folk art based on creation of patterns.

    Parameters:
    ----------
        size: int
            Rangoli size
    
    Returns: None
        Prints the alphabet rangoli
    """
    # Create a list of the alphabet
    alpha = string.ascii_lowercase

    # Width Rangoli
    width = 4 * size - 3

    # Build Rangoli
    for i in range(2 * size -1):
        k = abs(size - 1 - i)
        s = "-".join(alpha[size-1:k:-1] + alpha[k:size])
        print(s.center(width, "-"))

#############################################
# Run the main program
#############################################
if __name__ == "__main__":
    # Validate the value of "n"
    while True:
        try:
            N = int(input("Enter the value of N: ").strip())
            if N < 1 or N > 26:
                print("Please enter an integer between 1 and 26.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    print_rangoli(N)