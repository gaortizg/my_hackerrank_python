#############################################
# Import the necessary modules and functions
#############################################
from typing import cast

#############################################
# Define functions required for the program
#############################################
def get_valid_int(prompt: str) -> int:
    """
    Prompts the user for a positive integer input (2 <= n <= 5) and validates it. The function will continue to prompt the user until a valid input is received.

    Args:
        prompt (str): The message displayed to the user when asking for input.

    Returns:
        int: A valid positive integer input from the user.
    """
    while True:
        try:
            value = int(input(prompt).strip())
            if value < 2 or value > 5:
                print("Invalid input. Please enter a positive integer between 2 and 5.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter an integer between 2 and 5.")

#############################################
# Run the main program
#############################################
if __name__ == "__main__":
    n = get_valid_int("Enter the number of students: ")

    # Initialize records list and store information about students and their scores in a nested tuple
    records: list[tuple[str, float]] = []
    for _ in range(n):
        name = input(f"Enter student name {(_ + 1)}: ").strip()
        score = float(input(f"Enter the score of {name}: ").strip())

        student_score = (name, score)
        records.append(student_score)

    # Sort list from lowest score to highest score using a lambda function as the key, which extracts the score from each tuple for comparison
    sorted_by_last = sorted(records, key=lambda x: cast(float, x[1]))

    # Create a set of unique scores and sort it
    unique_scores = sorted({score for _, score in records})

    # Validate there are enough unique scores to determine the second lowest score
    if len(unique_scores) == 1:
        print("Not enough unique scores to determine the second lowest.")
    else:
        # Determine second lowest score, then take names with that score and print them in alphabetical order
        second = unique_scores[1]
        print(f"\nStudent(s) with the second lowest score:")
        print(*sorted(name for name, score in records if score == second), sep="\n")