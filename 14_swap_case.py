#############################################
# Define functions required for the program
#############################################
def swap_case(s: str) -> str:
    """
    This function takes a string as input and returns a new string where all uppercase letters
    are converted to lowercase and all lowercase letters are converted to uppercase.

    Parameters:
    s (str): The input string.

    Returns:
    str: The string with swapped cases.

    IMPORTANT NOTE:
    This function is for practice only. There's already a method in Pyhton that helps with this:
    s.swapcase()
    """
    swapped_s = ""
    for i in s:
        if i.isupper():
            swapped_s += i.lower()
        elif i.islower():
            swapped_s += i.upper()
        else:
            swapped_s += i
    
    return swapped_s

#############################################
# Run the main program
#############################################
if __name__ == "__main__":
    while True:
        try:
            s = input("Enter a string: ")
            if len(s) > 0 and len(s) <= 1000:
                break
        except ValueError:
            pass
        print("Invalid input. Please enter a string with 1 to 1000 characters.")

    # Print string with swapped cases
    print(swap_case(s))

