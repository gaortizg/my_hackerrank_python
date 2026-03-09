#############################################
# Define functions required for the program
#############################################
def count_substring(string: str, substring: str) -> int:
    """
    This function takes a string and counts the occurrences of a substring.

    Parameters:
    string (str): The input string.
    substring (str): The substring to count.

    Returns:
    int: The number of occurrences of the substring.
    """
    count = 0
    start = 0
    while True:
        pos = string.find(substring, start)
        if pos == -1:
            break
        count += 1
        start = pos + 1
    return count

#############################################
# Run the main program
#############################################
if __name__ == "__main__":
    # Validate string is not empty
    while not (string := input("Enter a string: ")):
        print("String cannot be empty.")

    # Validate substring is not empty
    while not (substring := input("Enter the substring to count: ")):
        print("Substring cannot be empty.")

    # Print the count of the substring
    print(count_substring(string, substring))