def is_leap(year):
    """
    Determine if a given year is a leap year.

    Args:
        year (int): The year to check.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

if __name__ == "__main__":
    # Validate input for 'year'(1900 <= year <= 10**5)
    while True:
        try:
            year = int(input("Enter integer year (1900-10**5): ").strip())
            if year < 1900 or year > 10**5:
                print("Invalid input. Please enter an integer between 1900 and 10**5.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer between 1900 and 10**5.")
            continue

    # Determine if the year is a leap year
    print(is_leap(year))