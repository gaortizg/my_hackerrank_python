#############################################
# Run the main program
#############################################
if __name__ == "__main__":
    # Validate string is not empty
    while not (0 < len(string := input("Enter a string: ")) <= 1000):
        print("String cannot be empty nor it can be longer than 1000 characters. Please try again.")

    has_alnum = has_alpha = has_digit = has_lower = has_upper = False

    for c in string:
        if c.isalnum():
            has_alnum = True
        if c.isalpha():
            has_alpha = True
        if c.isdigit():
            has_digit = True
        if c.islower():
            has_lower = True
        if c.isupper():
            has_upper = True

        # Optional early exit if everything is already True
        if all((has_alnum, has_alpha, has_digit, has_lower, has_upper)):
            break

    print(f"has_alnum: {has_alnum}")
    print(f"has_alpha: {has_alpha}")
    print(f"has_digit: {has_digit}")
    print(f"has_lower: {has_lower}")
    print(f"has_upper: {has_upper}")