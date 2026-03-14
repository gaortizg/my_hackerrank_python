#############################################
# Define functions required for the program
#############################################
def solve(s: str) -> None:
    """
    Make sure that each word in the string is capitalized

    Parameters:
    ----------
        s: str
            String to capitalize
    
    Returns: None
        Prints the string capitalized
    """
    # Split every word in full name
    words = s.split()
    
    print(" ".join(word[0].upper() + word[1:] for word in words))


#############################################
# Run the main program
#############################################
if __name__ == "__main__":
    # Validate string length
    while True:
        try:
            S = input("Enter full name: ").strip()
            if  1 <= len(S) <= 1000 and all(word.isalnum() for word in S.split()):
                break
        except ValueError:
            pass
        print("Invalid input. Please only enter an alphanumeric string with 1 to 1000 characters.")
    
    # Capitalize routine
    solve(S)