#############################################
# Define functions required for the program
#############################################
def print_formatted(number: int) -> None:
    """
    Prints the Decimal, Octal, Hexadecimal (capitalized), and Binary
    representations of each number in range(1,number+1)

    Parameters:
    ----------
        number: int
            Max numbers to convert
    
    Returns:
    ----------
        None: It only prints the different conversions
    """
    w = len(bin(number)[2:])

    # main loop
    for i in range(1, number+1):
        print(*(f"{x:>{w}} " for x in (i, oct(i)[2:], hex(i)[2:].upper(), bin(i)[2:])))

#############################################
# Run the main program
#############################################
if __name__ == "__main__":
    # Validate the value of "n"
    while True:
        try:
            n = int(input("Enter the value of n: ").strip())
            if n < 1 or n > 99:
                print("Please enter an integer between 1 and 99.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    print_formatted(n)